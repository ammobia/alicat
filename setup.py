"""Install parameters for CLI and python import."""
from setuptools import setup

with open('README.md', 'r') as in_file:
    long_description = in_file.read()

setup(
    name="alicat",
    version="0.4.1",
    description="Python driver for Alicat mass flow controllers.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/numat/alicat/",
    author="Patrick Fuller",
    author_email="pat@numat-tech.com",
    packages=["alicat"],
    install_requires=["pyserial"],
    entry_points={
        "console_scripts": [("alicat = alicat:run")]
    },
    license="GPLv2",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Development Status :: 4 - Beta",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Human Machine Interfaces",
    ]
)
