# Erik Williams
# CPSC 386-02
# 2023-03-23
# epwilliams@csu.fullerton.edu
# @EPW80
#
# Lab 00-00
#
# This my pygame project!
#

""" Simple setup.py """

from setuptools import setup

setup_info = {
    "name": "videogame",
    "version": "0.1",
    "description": "A package to support writing games with PyGame",
    "long_description": open("README.md").read(),
    "long_description_content_type": "text/markdown",
    "author": "EPW80",
    "author_email": "epwilliams@csu.fullerton.edu",
    "url": "https://github.com/cpsc-spring-2023/cpsc-386-04-scene-EPW80",
    "license": "MIT",
    "classifiers": [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    "packages": ["videogame"],
    "install_requires": [
        "pygame",
        # Add any additional dependencies your project requires
    ],
}

setup(**setup_info)
