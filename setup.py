#!/usr/bin/env python3
import os

from setuptools import find_packages, setup

def exec_file(path_segments):
  """Execute a single python file to get the variables defined in it"""
  result = {}
  code = read_file(path_segments)
  exec(code, result)
  return result

def read_file(path_segments):
  """Read a file from the package. Takes a list of strings to join to
  make the path"""
  file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), *path_segments)
  with open(file_path) as f:
    return f.read()

version = exec_file(("rudy", "__init__.py"))["__version__"]
long_description = read_file(("README.md",))

setup(
  name="rudy",
  version=version,
  url="https://github.com/ballofcthulu/rudy",
  description="A really stupid Matrix bod",
  packages=find_packages(exclude=["tests", "tests.*"]),
  install_requires=[
    "matrix-nio[e2e]>=0.10.0",
    "nltk>=3.6.2",
  ],
  classifiers=[
    "License :: OSI Approved :: The Unlicense (Unlicense)",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
  ],
  long_description=long_description,
  long_description_content_type="text/markdown",

  scripts=["bin/rudy"],
)
