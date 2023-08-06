from setuptools import setup, find_packages
import datacontainerqnp as dc

setup(
    name="datacontainerqnp",
    version=dc.__version__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "stockutilitiesqnp",
        "pandas",
        "requests"
    ],
)