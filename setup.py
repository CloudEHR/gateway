from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name='cloudehr-gateway',
    version='0.1dev0',
    author='Chrysostomos Symvoulidis', 
    author_email='simvoul@unipi.gr',
    packages=find_packages(),
    long_description=open('README.md').read()
)