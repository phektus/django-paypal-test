#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='hr_payment',
      version='0.1',
      packages=find_packages(),
      package_data={'hr_payment': ['bin/*.*', 'static/*.*', 'templates/*.*']},
      exclude_package_data={'hr_payment': ['bin/*.pyc']},
      scripts=['hr_payment/bin/manage.py'])
