#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# NOTE : These directories are pushed to the website separately.
list_of_prohibted_directories = ['eme185-uploads',
                                 'icsc2017',
                                 'icsc2017.old',
                                 'jkm',
                                 'mech-cap',
                                 'misc',
                                 'presentations',
                                 'zotero']

files_and_dirs = os.listdir('content/pages')
msg = "{} can't be a directory name because it conflicts with one on the server."
for f in files_and_dirs:
    if f in list_of_prohibted_directories:
        raise ValueError(msg.format(f))

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
