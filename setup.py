#!/usr/bin/env python
import os

from setuptools import find_packages, setup


def read(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


setup(
    name="django-findreplace",
    version="0.1",
    description="Django Find Replace",
    long_description=read("README.rst"),
    long_description_content_type="text/x-rst",
    url="https://github.com/developersociety/django-findreplace",
    maintainer="The Developer Society",
    maintainer_email="studio@dev.ngo",
    platforms=["any"],
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=["Django>=1.11"],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.2",
    ],
    license="BSD",
)
