#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages
import os
import sys

py_version = sys.version_info
version = "0.1"
readme = os.path.join(os.path.dirname(__file__), 'README.rst')

CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Natural Language :: English',
    'Topic :: Utilities'
]

install_requires = [
    'six',
    'simplejson',
    'pytz',
    'django==1.9.1',
]


if isinstance(py_version, tuple):
    if py_version < (2, 7):
        install_requires.append('importlib')


setup(
    name='djtp_watcher',
    author='Nickolas Fox <tarvitz@blacklibrary.ru>',
    version=version,

    author_email='tarvitz@blacklibrary.ru',
    url='http://pypi.python.org/pypi/djtp-watcher',

    download_url='https://github.com/tarvitz/djtp-watcher/archive/master.zip',
    description='Django boilerplate project watcher',
    long_description=open(readme).read(),
    license='MIT license',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=install_requires,
    packages=find_packages(
        exclude=['tests', ]
    ),
    test_suite='tests',
    include_package_data=True,
    zip_safe=False)
