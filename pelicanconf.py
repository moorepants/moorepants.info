#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import yaml

AUTHOR = 'Jason K. Moore'
SITENAME = 'moorepants'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# This sets the default pages to be top level items and articles to be under
# /blog/.
INDEX_SAVE_AS = 'blog/index.html'
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
MENUITEMS = [('Blog', '/blog/')]
READERS = {'html': None}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

try:
    with open('config.yml', 'r') as config_file:
        config_data = yaml.load(config_file, Loader=yaml.FullLoader)
except IOError:
    THEME = ''
    PLUGIN_PATHS = ['']
else:
    THEME = config_data['THEME_PATH']
    PLUGIN_PATHS = [config_data['PLUGIN_PATHS']]

# Alchemy theme settings
SITESUBTITLE = 'a websitee'
SITEIMAGE = 'https://moorepants.s3.us-east-005.dream.io/headshot.jpg'
DESCRIPTION = ''
#GOOGLE_ANALYTICS = ''
#DISQUS_SITENAME = ''

# Alchemy theme settings that are custom to our fork: mechmotum branch
# If a Twitter username is provided a feed of the tweets will be displayed on
# the front page of the website.
ARTICLE_LIST_SUBTITLE = 'Blog'
# excludes these categories from the main blog list
EXCLUDED_CATEGORIES = ['notebook']
# pelican-alchemy removed the original theme.css, so bring it back.
THEME_CSS_OVERRIDES = ['theme/css/origtheme.css']

## PLUGINS

PLUGINS = ['render_math', 'extract_toc']
