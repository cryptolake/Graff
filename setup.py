# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='graff',
    version='1.0',
    description='A Minimal HTML only blog posts generator',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='cryptolake',
    author_email='dhiadah@gmail.com',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    url='https://github.com/cryptolake/graff',
    python_requires='>=3.6',
    license=license,
)
