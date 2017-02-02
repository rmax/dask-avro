import dask_avro


def test_package_metadata():
    assert dask_avro.__author__
    assert dask_avro.__email__
    assert dask_avro.__version__
