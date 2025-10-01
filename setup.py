"""
Setup configuration for entityidentity-installtest package
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="entityidentity-installtest",
    version="1.0.0",
    author="Peter Cotton",
    description="Test suite and examples for the entityidentity package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/microprediction/entityidentity-installtest",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        "entityidentity>=0.0.2",
        "pytest>=7.0.0",
        "pandas>=1.3.0",
    ],
    extras_require={
        "dev": [
            "pytest-cov",
            "black",
            "flake8",
        ],
    },
    entry_points={
        "console_scripts": [
            "entityidentity-test=tests.run:main",
            "entityidentity-examples=tests.examples:main",
        ],
    },
)

