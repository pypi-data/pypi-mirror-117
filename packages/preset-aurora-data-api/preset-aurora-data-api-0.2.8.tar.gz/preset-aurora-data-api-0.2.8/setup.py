#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="preset-aurora-data-api",
    version="0.2.8",
    url='https://github.com/preset-io/aurora-data-api',
    license='Apache Software License',
    author='Andrey Kislyuk',
    author_email='akislyuk@chanzuckerberg.com',
    description=(
        'A Python DB-API 2.0 client for the AWS Aurora Serverless Data API. '
        'This is a temporary package that allows credentials to be passed '
        'via the SQLAlchemy URI'
    ),
    long_description=open('README.rst').read(),
    install_requires=[
        'boto3 >= 1.9.245, < 2'
    ],
    extras_require={
    },
    packages=find_packages(exclude=['test']),
    platforms=['MacOS X', 'Posix'],
    test_suite='test',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
