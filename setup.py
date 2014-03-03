#!/usr/bin/env python

from distutils.core import setup
from distutils.core import Command

setup(name="RSS Eater",
      version="0.1",
      description="Download content from RSS feeds",
      author="Nabil Alsharif",
      author_email="blit32@gmail.com",
      license="MIT",
      scripts=["bin/rsseater"]
)
