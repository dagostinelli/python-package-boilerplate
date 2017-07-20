from setuptools import setup, find_packages

version = open('VERSION').read().strip()

setup(
    name = 'python-package-boilerplate',
    version = version,
    author = 'Your Name Here',
    author_email = 'you@somewhere.com',
    url = 'http://www.somewhere.com',
    description = 'Lorem ipsum dolor fiat lux',
    long_description = open('README.md').read().strip(),
    packages = find_packages('packagename'),
    install_requires=[
        # put packages here
        'six',
    ],
    test_suite = 'tests',
)
