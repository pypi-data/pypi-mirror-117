#!/usr/bin/env python

# Original work Copyright (c) Facebook, Inc. and its affiliates.
# Modified work Copyright (c) 2021 Sartorius AG

from setuptools import setup
import torch
from torch.utils.cpp_extension import CppExtension
import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

def get_extensions():

    print("retriving extentions!")

    sources = ["csrc/coco_eval/cocoeval.cpp", "csrc/vision.cpp"]

    extension = CppExtension
    include_dirs = []

    print(f"Sources: {sources}")

    ext_modules = [
        extension(
            name="fast_coco_eval._C",
            sources=sources,
            language='c++'
        )
    ]

    return ext_modules

classifiers=[

    'Development Status :: 3 - Alpha',

    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Topic :: Software Development :: Libraries :: Python Modules',

    'License :: OSI Approved :: Apache Software License',

    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
]

setup(
    name="fast-coco-eval",
    version="1.0",
    author="Christoffer Edlund",
    python_requires=">=3.6",
    ext_modules=get_extensions(),
    packages=setuptools.find_packages(),
    cmdclass={"build_ext": torch.utils.cpp_extension.BuildExtension},
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=classifiers,
    install_requires=[
        'torch>=1.4.0',
        'numpy',
        "pybind11",
        "pycocotools"
    ],
)
