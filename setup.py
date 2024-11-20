# setup.py

from setuptools import setup, find_packages

setup(
    name="ai_smif_v2",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'pytest',
    ],
)