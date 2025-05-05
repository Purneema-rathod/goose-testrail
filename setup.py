from setuptools import setup, find_packages

setup(
    name="goose-testrail",
    version="0.1.0",
    description="TestRail extension for Goose",
    author="Purnee Marathod",
    author_email="purneemarathod@gmail.com",
    packages=find_packages(),
    install_requires=[
        "goose-core>=0.1.0",  # Adjust version as needed
    ],
    include_package_data=True,
    package_data={
        "": ["manifest.yaml"],
    },
)