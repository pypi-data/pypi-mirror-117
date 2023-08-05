import os.path
import re

from setuptools import find_packages, setup

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))


def get_long_description():
    return open(os.path.join(ROOT_DIR, "README.md"), encoding="utf-8").read()


def get_version():
    """Read the version from a file (liquichain/api/version.py) in the repository.

    We can't import here since we might import from an installed version.
    """
    version_file = open(os.path.join(ROOT_DIR, "liquichain", "api", "version.py"), encoding="utf=8")
    contents = version_file.read()
    match = re.search(r'VERSION = [\'"]([^\'"]+)', contents)
    if match:
        return match.group(1)
    else:
        raise RuntimeError("Can't determine package version")


setup(
    name="liquichain-api-python",
    version=get_version(),
    license="BSD",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    description="Liquichain API client for Python",
    author="Liquichain",
    author_email="contact@liquichain.io",
    maintainer="Manaty SARL",
    maintainer_email="contact@manaty.net",
    keywords=[
        "liquichain",
        "blockchain",
        "cryptocurrency",
        "payment",
        "service",
        "direct debit",
        "refunds",
        "payments",
        "gateway",
    ],
    url="https://github.com/liquichain/Liquichain-api-python",
    install_requires=[
        "requests",
        "urllib3",
        "requests_oauthlib",
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Topic :: Office/Business :: Financial",
    ],
)
