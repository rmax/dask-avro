#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io

from pkgutil import walk_packages
from setuptools import setup


def find_packages(path):
    # This method returns packages and subpackages as well.
    return [name for _, name, is_pkg in walk_packages([path]) if is_pkg]


def read_file(filename):
    with io.open(filename) as fp:
        return fp.read().strip()


def read_rst(filename):
    content = read_file(filename)
    # Ignore unsupported directives by pypi.
    return ''.join(line for line in io.StringIO(content)
                   if not line.startswith('.. comment::'))


def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]


setup_attrs = dict(
    name='dask-avro',
    version=read_file('VERSION'),
    description="Avro reader for Dask.",
    long_description=read_rst('README.rst') + '\n\n' + read_rst('HISTORY.rst'),
    author="Rolando (Max) Espinoza",
    author_email='rolando@rmax.io',
    url='https://github.com/rmax/dask-avro',
    packages=list(find_packages('src')),
    package_dir={'': 'src'},
    install_requires=read_requirements('requirements.txt'),
    include_package_data=True,
    license="MIT",
    keywords='dask-avro',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)


if __name__ == "__main__":
    setup(**setup_attrs)
