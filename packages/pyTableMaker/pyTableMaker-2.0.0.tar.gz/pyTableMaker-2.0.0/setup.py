import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="pyTableMaker",
    version="2.0.0",
    description="The module to create, edit and show tables conveniently.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/windowsboy111/pyTableMaker",
    author="windowsboy111",
    author_email="wboy111@outlook.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["pyTableMaker"],
)
