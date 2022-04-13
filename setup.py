import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), f'{fname}.md')).read()

setup(
    name = "xorg_resolution_fixer",
    version = "1.0.0",
    author = "Paride Giunta",
    author_email = "paridegiunta@gmail.com",
    description = ("A python module that uses xrandr and cvt to force a specific resolution"),
    license = "MIT",
    keywords = "xorg resolution xrandr",
    entry_points = {
        'console_scripts': ['xrf=xorg_resolution_fixer:main'],
    },
    url = "https://github.com/jasoc/xorg-resolution-fixer",
    packages=['xorg_resolution_fixer'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
)