from setuptools import setup, find_packages
from resizePixel.version import Version
import os

here = os.path.abspath(os.path.dirname(__file__))

with open("README.md", "r") as fh:
    long_description = fh.read()


VERSION = '0.0.1'
DESCRIPTION = 'Python Resize Pixel'
LONG_DESCRIPTION = open('README.md').read().strip()



# Setting up
setup(name='resizePixel',
    version=Version('1.0.0').number,
    author="mkshgh",
    author_email="<mukesh.ghimire@outlook.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['pytest', 'pytest-cov'],
    keywords=['python', 'image', 'image quality', 'reduce', 'increase', 'frustrated'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>3.7',
    )
