# -*- coding: utf-8 -*-

from setuptools import setup


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
    url='https://github.com/cryptolake/graff',
    license=license,
)
