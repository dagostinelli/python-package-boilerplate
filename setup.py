from setuptools import setup, find_packages

version = open('VERSION').read().strip()
license = open('LICENSE').read().strip()

setup(
    name = 'python-package-boilerplate',
    version = version,
    license = license,
    author = 'Your Name Here',
    author_email = 'you@somewhere.com',
    url = 'http://www.somewhere.com',
    description = 'Lorem ipsum dolor fiat lux',
    long_description = open('README.md').read().strip(),
    packages = find_packages(),
    install_requires=[
        # put packages here
        'six',
    ],
    test_suite = 'tests',
    entry_points = {
	    'console_scripts': [
	        'packagename = packagename.__main__:main',
	    ]
	}
)
