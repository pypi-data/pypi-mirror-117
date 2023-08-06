from setuptools import setup, version


__project__ = "colorgnomehat"
__version__ = "0.0.1"
__description__ = "a python program that will generate colors for text and variables"
__packages__ = ["colorgnomehat"]
__author__ = "Rigved Aneesh"
__author_email__ = "rigved.bob@gmail.com"
#copied from raspberrypi projects
__classifiers__ = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Education",
    "Programming Language :: Python :: 3",
]
__keywords__ = ["color", "text"]

setup(   
    name = __project__,
    version = __version__,
    description = __description__,
    packages = __packages__,
    author = __author__,
    author_email = __author_email__,
    classifiers = __classifiers__ 
)

