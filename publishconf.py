#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
if os.environ['TRAVIS'] == 'true':
    SITEURL = 'https://moorepants.info.github.io'
    THEME = "pelican-alchemy/alchemy"
    PLUGIN_PATHS = "pelican-plugins"
else:
    SITEURL = 'https://moorepants.info'
    DISQUS_SITENAME = "moorepants"
    GOOGLE_ANALYTICS = "UA-15966419-6"

RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True
