#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='dirmon',
      version='1.0',
      description='Easy directory monitoring',
      author='Alex Yancey',
      author_email='alexyancey3@gmail.com',
      url='https://github.com/ayancey/dirmon',
      py_modules=['dirmon'],
     )