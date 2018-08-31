# coding=utf-8

import os
import sys
import setuptools

# here = os.path.abspath(os.path.dirname(__file__))

# 'setup.py publish' shortcut.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload --repository-url https://test.pypi.org/legacy/ dist/*')
    sys.exit()

packages = ['distribute_test']

# requires = ['requests>=2.11.0']
requires = ['requests']

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="distribution-test-pkg",
    version="2.0.2",
    author="Young Kang",
    author_email="kangyy666@gmail.com",
    description="A small test package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KangStark/distribute-test-pkg",
    packages=packages,
    package_data={'': ['LICENSE', 'NOTICE']},
    include_package_data=True,
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    install_requires=requires,
    license='Apache 2.0',
    zip_safe=False,
    classifiers=(
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent"
    )
)
