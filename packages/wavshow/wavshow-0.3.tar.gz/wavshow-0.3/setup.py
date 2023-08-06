#!/usr/bin/env python

import pathlib
from setuptools import setup, find_packages

setup(
  name='wavshow',
  version='0.3',
  license='MIT',
  author="mzmttks",
  author_email="ta.mizumoto@gmail.com",
  url="https://github.com/mzmttks/wavshow",
  packages=find_packages(),
  insatll_requires=pathlib.Path("requirements.txt").read_text().rstrip().split("\n"),
  entry_points = {
    "console_scripts":{
      "wavshow=wavshow:main"
    }
  }
)
