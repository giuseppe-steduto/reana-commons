# -*- coding: utf-8 -*-
#
# This file is part of REANA.
# Copyright (C) 2018, 2019, 2020, 2021, 2022, 2023 CERN.
#
# REANA is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""REANA-Commons."""

from __future__ import absolute_import, print_function

import os
import re

from setuptools import find_packages, setup

readme = open("README.md").read()
history = open("CHANGELOG.md").read()

tests_require = [
    "pytest-reana>=0.9.2,<0.10.0",
]


extras_require = {
    "docs": [
        "myst-parser",
        "Sphinx>=1.5.1",
        "sphinx-rtd-theme>=0.1.9",
    ],
    "tests": tests_require,
    "kubernetes": [
        "kubernetes>=22.0.0,<23.0.0",
    ],
    "yadage": ["adage~=0.10.1", "yadage~=0.20.1", "yadage-schemas~=0.10.6"],
    "cwl": ["cwltool==3.1.20210628163208"],
    "snakemake": [
        "snakemake==6.15.5 ; python_version<'3.7'",  # Snakemake v7 requires Python 3.7+
        "snakemake==7.32.4 ; python_version>='3.7'",
        "tabulate<0.9",
        "pulp>=2.7.0,<2.8.0",
    ],
    "snakemake_reports": [
        "snakemake==6.15.5 ; python_version<'3.7'",
        "snakemake==7.32.4 ; python_version>='3.7'",
        "pygraphviz<1.8",
        "tabulate<0.9",  # tabulate 0.9 crashes snakemake, more info: https://github.com/snakemake/snakemake/issues/1899
        "pulp>=2.7.0,<2.8.0",
    ],
}

extras_require["all"] = []
for key, reqs in extras_require.items():
    if ":" == key[0]:
        continue
    extras_require["all"].extend(reqs)

setup_requires = [
    "pytest-runner>=2.7",
]

install_requires = [
    "bravado>=10.2,<10.4",
    # bravado-core 6.1.1 breaks compatibility with jsonschema<4.9.0
    # see https://github.com/reanahub/reana-commons/issues/430
    "bravado-core<6.1.1",
    "checksumdir>=1.1.4,<1.2",
    "click>=7.0",
    "fs>=2.0",
    "jsonschema[format]>=3.0.1,<4.0.0",
    "kombu>=4.6",
    "mock>=3.0,<4",
    "PyYAML>=5.1,<7.0",
    "Werkzeug>=0.14.1",
    "wcmatch>=8.3,<8.5",
]

packages = find_packages()


# Get the version string. Cannot be done with import!
with open(os.path.join("reana_commons", "version.py"), "rt") as f:
    version = re.search(r'__version__\s*=\s*"(?P<version>.*)"\n', f.read()).group(
        "version"
    )

setup(
    name="reana-commons",
    version=version,
    description=__doc__,
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/markdown",
    author="REANA",
    author_email="info@reana.io",
    url="https://github.com/reanahub/reana-commons",
    packages=[
        "reana_commons",
    ],
    zip_safe=False,
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=install_requires,
    extras_require=extras_require,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
