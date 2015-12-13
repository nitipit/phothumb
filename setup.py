#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='phothumb',
    version='1.2',
    packages=find_packages(),
    description='Photo thumbnail library based on Pillow',
    author='Nitipit Nontasuwan',
    author_email='nitipit@gmail.com',
    license='MIT',
    keywords='photo image thumbnail',
    install_requires=['pillow',],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    url='https://github.com/nitipit/phothumb',
)
