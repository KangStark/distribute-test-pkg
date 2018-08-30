# coding=utf-8

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="distribution-test-pkg",
    version="0.0.2",
    author="Young Kang",
    author_email="kangyy666@gmail.com",
    description="A small test package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KangStark/distribute-test-pkg",
    packages=setuptools.find_packages(exclude=["test*"]),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    )
)
