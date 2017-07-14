import os

import dask_avro


TESTS_DIR = os.path.dirname(__file__)
AVRO_TEST_FILE = os.path.join(TESTS_DIR, 'top-1m.deflate.avro')


def test_dask_avro():
    # If partitions are larger than avro internal partitions some blocks
    # may be empty.
    partitions = 3
    blocksize = (os.path.getsize(AVRO_TEST_FILE) + partitions) // partitions
    values = dask_avro.read_avro(AVRO_TEST_FILE, blocksize=blocksize)
    assert len(values) == partitions
    for d in values:
        blocks = list(d.compute())
        assert len(blocks) > 0
