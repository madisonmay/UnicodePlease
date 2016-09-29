try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="unicode-please",
    version="0.1.0",
    packages=["unicode_please"],
    author="Madison May",
    author_email="""
        Madison May <madison@indico.io>
    """,
    description="""
        Utilities to prevent you from tearing your hair out
        dealing with unicode and text encodings in python 2.7
    """,
    install_requires=[
        "chardet >= 2.0.0"
    ]
)
