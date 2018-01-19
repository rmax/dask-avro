=========
Dask-Avro
=========

.. image:: https://img.shields.io/pypi/v/dask-avro.svg
        :target: https://pypi.python.org/pypi/dask-avro

.. image:: https://img.shields.io/pypi/pyversions/dask-avro.svg
        :target: https://pypi.python.org/pypi/dask-avro

.. image:: https://readthedocs.org/projects/dask-avro/badge/?version=latest
        :target: https://readthedocs.org/projects/dask-avro/?badge=latest
        :alt: Documentation Status

.. image:: https://img.shields.io/travis/rmax/dask-avro.svg
        :target: https://travis-ci.org/rmax/dask-avro

.. image:: https://codecov.io/github/rmax/dask-avro/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/rmax/dask-avro

.. image:: https://landscape.io/github/rmax/dask-avro/master/landscape.svg?style=flat
    :target: https://landscape.io/github/rmax/dask-avro/master
    :alt: Code Quality Status

.. image:: https://requires.io/github/rmax/dask-avro/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/rmax/dask-avro/requirements/?branch=master

Avro reader for Dask.

* Free software: MIT license
* Documentation: https://dask-avro.readthedocs.org.
* Python versions: 2.7, 3.4+

Features
--------

This projects provides an Avro_ format reader for Dask_. Provides a convenient
function to read one or more Avro files and partition them arbitrarily.

Quickstart
----------

Usage::

  import dask.bag
  import dask_avro

  delayeds = dask_avro.read_avro("data-*.avro", blocksize=2**26)
  data = dask.bag.from_delayed(delayeds)


Credits
-------

This package was created with Cookiecutter_ and the `rmax/cookiecutter-pypackage`_ project template.

.. _Avro: https://avro.apache.org/docs/1.2.0/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Dask: http://dask.pydata.org/en/latest/
.. _`rmax/cookiecutter-pypackage`: https://github.com/rmax/cookiecutter-pypackage
