# https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56
from distutils.core import setup
from setuptools import setup, find_packages
from _version import __version__

setup(
    name="deimport",
    packages=find_packages(),
    version=__version__,
    license="MIT",
    description="Simple package to deimport python modules",
    author="Mahmoud Soliman",
    author_email="mjs@aucegypt.edu",
    url="https://github.com/mjsml/deimport",
    download_url="https://github.com/mjsml/deimport/releases",
    keywords=["setup", "runtime", "automation"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    
)
