from setuptools import setup, find_packages
import stockutilitiesqnp as util

setup(
    name="stockutilitiesqnp",
    version=util.__version__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "python-dateutil==2.8.1"
    ],
)