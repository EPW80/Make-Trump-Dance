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
    # TODO: Optional, add more information to the setup.py script
    # "long_description": open("README.md").read(),
    "author": "EPW80",
    "author_email": "epwilliams@csu.fullerton.edu",
    # "url": "https://some.url/somehwere/maybe/github",
}

setup(**setup_info)
