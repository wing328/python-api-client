# coding: utf-8

"""
    Quant Trading Network API

    This API will use JSON.         JSON looks like this:                {         \"key\": \"value\",         \"anotherKey\": \"anotherValue\"       }  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@quant-trading.network
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "quant-trading-api"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    license="MIT",
    description="Quant Trading Network API",
    author = "Quant-trading.Network",
    author_email="support@quant-trading.network",
    url="https://github.com/Quant-Network/python-api-client",
    download_url = "https://github.com/Quant-Network/python-api-client/archive/v_1.tar.gz",
    keywords=["Quant Trading Network API", "algorithmic trading", "trading", "bitcoin", "Swagger"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    This API will use JSON.         JSON looks like this:                {         \&quot;key\&quot;: \&quot;value\&quot;,         \&quot;anotherKey\&quot;: \&quot;anotherValue\&quot;       }  # noqa: E501
    """,
    classifiers=[
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Build Tools",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",],
)
