import fastavro


_stream_wrapper = None
if fastavro.__version_info__ >= (0, 19, 7):
    _iter_avro = fastavro._read._iter_avro_records
elif fastavro.__version_info__ >= (0, 17, 0):
    _iter_avro = fastavro._read._iter_avro
    _stream_wrapper = fastavro._read.FileObjectReader
else:
    raise ImportError("Unsupported fastavro version: %s" % fastavro.__version__)


def iter_avro(stream, header, codec, writer_schema, reader_schema):
    """Expose internal _iter_avro."""
    if _stream_wrapper is not None:
        stream = _stream_wrapper(stream)

    return iter(_iter_avro(stream, header, codec, writer_schema, reader_schema))
