import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), f'{fname}.md')).read()

setup(
    name = "xorg_resolution_fixer",
    version = "0.0.5",
    author = "Paride Giunta",
    author_email = "paridegiunta@gmail.com",
    description = (""),
    license = "MIT",
    keywords = "xorg resolution xrandr",
    entry_points = {
        'console_scripts': ['xrf=xorg_resolution_fixer:main'],
    },
    url = "http://packages.python.org/an_example_pypi_project",
    packages=['xorg_resolution_fixer'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
)