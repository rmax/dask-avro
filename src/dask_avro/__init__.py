# -*- coding: utf-8 -*-
"""A fastavro-based avro reader for Dask.

Disclaimer: The initial code was recovered from dask's distributed project.

"""
import io
import itertools
import json

import fastavro

from dask import delayed
from dask.bytes import read_bytes
from dask.bytes.core import OpenFileCreator


__author__ = 'Rolando (Max) Espinoza'
__email__ = 'me at rmax.io'
__version__ = '0.1.1'


def read_avro(urlpath, blocksize=2**27, **kwargs):
    """Reads avro files.

    Parameters
    ----------
    urlpath : str or list[str]
        Absolute or relative filepath, URL or globstring pointing to avro files.
    blocksize : int, optional
        Size of blocks. Note that this size must be larger than the files'
        internal block size, otheriwse it will result in empty partitions.
        Default is 128MB.
    **kwargs
        Additional arguments passed to ``dask.bytes.read_bytes`` function.

    Returns
    -------
    out : list[Delayed]
        A list of delayed objects, one for each block.

    """
    if isinstance(urlpath, str):
        urlpath = [urlpath]
    if not isinstance(urlpath, list):
        raise TypeError("Invalid type for 'urlpath': %s" % type(urlpath))

    return list(itertools.chain.from_iterable(
        _read_avro(path, blocksize=blocksize, **kwargs) for path in urlpath
    ))


def _read_avro(urlpath, **kwargs):
    """Read avro file in given path and returns a list of delayed objects."""
    myopen = OpenFileCreator(urlpath)

    values = []
    for fn in myopen.fs.glob(urlpath):

        with myopen(fn) as fp:
            av = fastavro.reader(fp)
            header = av._header

        # TODO: If the avro block size in the file is larger than the blocksize
        # passed here then some returned blocks may be empty because they don't
        # contain the delimiter.
        _, blockss = read_bytes(fn, delimiter=header['sync'], not_zero=True,
                                sample=False, **kwargs)
        values.extend(
            delayed(_avro_body)(block, header) for blocks in blockss for block in blocks
        )

    if not values:
        raise ValueError("urlpath is empty: %s" % urlpath)

    return values


def _avro_body(data, header):
    """Returns records for given avro data fragment."""
    stream = io.BytesIO(data)
    schema = json.loads(header['meta']['avro.schema'].decode())
    codec = header['meta']['avro.codec'].decode()
    return iter(fastavro._reader._iter_avro(stream, header, codec, schema, schema))
