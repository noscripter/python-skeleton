try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "description"      : "python-skeleton",
    "author"           : "noscripter",
    "url"              : "https: //github.com/noscripter/python-skeleton",
    "download_url"     : "https: //github.com/noscripter/python-skeleton",
    "author_email"     : "noscripter@github.com",
    "version"          : "0.1",
    "install_requiers" : ["nose"],
    "package"          : ["NAME"],
    "scripts"          : [],
    "name"             : "python-skeleton"
}

setupt(**config)
