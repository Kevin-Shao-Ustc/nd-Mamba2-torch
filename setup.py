"""Setup Torch Mamba."""

from setuptools import find_packages, setup


setup(
    name="torchnssd",
    version="0.1.0",
    description="torch realization of mamba2",
    packages=find_packages(),
    python_requires=">=3.9",
)