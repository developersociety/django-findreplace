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
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/developersociety/django-findreplace",
    maintainer="The Developer Society",
    maintainer_email="studio@dev.ngo",
    platforms=["any"],
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    python_requires=">=3.9",
    install_requires=["Django>=3.2"],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.2",
    ],
    license="BSD",
)
