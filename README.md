python-package-boilerplate
==========================

[![Build Status](https://travis-ci.org/dagostinelli/python-package-boilerplate.png?branch=master)](https://travis-ci.org/dagostinelli/python-package-boilerplate)
[![Requirements Status](https://requires.io/github/dagostinelli/python-package-boilerplate/requirements.svg?branch=master)](https://requires.io/github/dagostinelli/python-package-boilerplate/requirements/?branch=master)

A terse boilerplate for Python packages.  Where other boilerplates contain a great many features such as a CLI, docs, code coverage and varying opinions on what a unit test should look like, this one aims to be lean and mean.  I use this on my own projects.

## Package

The package structure is:

```
├── packagename
│   ├── __init__.py
│   └── somemodule.py
└── tests
│   ├── __init__.py
│   ├── test_myclass.py
│   └── test_mysecondclass.py
├── setup.py
├── .travis.yml
├── .gitignore
├── README.md
├── LICENSE
└── VERSION
```

## Requirements

Package requirements are handled using setup.py. They will be automatically installed on install or during unit testing

## Unit Tests

Testing is set up using the built in Unit Test framework in Python

Run the tests with `python setup.py test` in the root directory or use the handy `test.sh` script in the `/scripts` folder.

## Travis CI

There is a `.travis.yml` file that will execute the build and the unit tests against several versions of Python.

## Quick Start

```
git clone https://github.com/dagostinelli/python-package-boilerplate
cd python-package-boilerplate
virtualenv venv
source venv/bin/activate
cd scripts
./build.sh
./test.sh
```

Then begin renaming things and keep running those unit tests as you go.

## Nice to Add

I enjoy filesystem monitors that look for files as I change them and then automatically execute the unit tests in the background.  I haven't found a cross-platform way to do that yet, so it's not in this boilerplate.
