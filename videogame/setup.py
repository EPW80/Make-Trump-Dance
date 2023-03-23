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
