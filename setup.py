# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in balatest/__init__.py
from balatest import __version__ as version

setup(
	name='balatest',
	version=version,
	description='test',
	author='bala',
	author_email='bala@yuvabe.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
