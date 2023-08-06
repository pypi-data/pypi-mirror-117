#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DLC2Action Toolbox
© A. Mathis Lab
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dlc2action",
    version="0.0b0",
    author="A. Mathis Lab",
    author_email="alexander@deeplabcut.org",
    description="tba",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amathislab/DLC2Action",
    install_requires=[
        "tqdm",
    ],
    include_package_data=True,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
    ),
)
