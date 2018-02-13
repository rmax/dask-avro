import fastavro


try:
    _iter_avro = fastavro._read._iter_avro
    _stream_wrapper = fastavro._read.FileObjectReader
except AttributeError:  # fastavro < 0.16
    _iter_avro = fastavro._reader._iter_avro
    _stream_wrapper = None


def iter_avro(stream, header, codec, writer_schema, reader_schema):
    """Expose internal _iter_avro."""
    if _stream_wrapper is not None:
        stream = _stream_wrapper(stream)

    return iter(_iter_avro(stream, header, codec, writer_schema, reader_schema))
