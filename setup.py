from setuptools import setup
from pathlib import Path

code = Path(__file__).parent

readme = (code / "README.md").read_text()
requirements = (code / "requirements.txt")

with open(requirements) as requirements:
    requirements = requirements.readlines()
    requirements = [requirement.replace("\n", "") for requirement in requirements]

setup(
    name = "spotifyoffline",
    version = "v0.0.1",
    description = "listen to your favorite spotify songs, offline",
    long_description = readme,
    long_description_content_type = "text/markdown",
    url = "https://github.com/0x44RU5H/spotifyoffline",
    author = "Aarush Gupta",
    author_email = "aarush@theaarushgupta.com",
    license = "AGPLv3+",
    classifiers = [
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8"
    ],
    packages = ["spotifyoffline"],
    package_data = {},
    install_requires = requirements,
    entry_points = {
        "console_scripts": ["spotifyoffline = spotifyoffline.main:main"]
    }
)