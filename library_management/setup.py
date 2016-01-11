# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='library_management',
    version=version,
    description='manage all library transaction',
    author='nikhil',
    author_email='ranjanenikhil@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
