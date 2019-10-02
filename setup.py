#!/usr/bin/env python
from setuptools import find_packages, setup


setup(
    name='django-findreplace',
    version='0.1a1',
    description='Django Find Replace',
    long_description='Django Find Replace',
    url='https://github.com/developersociety/django-findreplace',
    maintainer='The Developer Society',
    maintainer_email='studio@dev.ngo',
    platforms=['any'],
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    python_requires='>=3.4',
    install_requires=['Django>=1.8'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.2',
    ],
    license='BSD',
)
