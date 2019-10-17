#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

try:
    os.environ['TRAVIS']
except KeyError:  # not on Travis
    SITEURL = 'https://moorepants.info'
    DISQUS_SITENAME = "moorepants"
    GOOGLE_ANALYTICS = "UA-15966419-6"
else:
    SITEURL = 'https://moorepants.github.io/moorepants.info'
    # NOTE : The theme and plugins are installed alongside this file on the
    # Travis build.
    THEME = "pelican-alchemy/alchemy"
    PLUGIN_PATHS = "pelican-plugins"
    MENUITEMS = [('Blog', '{}/blog/'.format(SITEURL))]

RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True
