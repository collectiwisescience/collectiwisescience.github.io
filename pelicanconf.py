#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Johannes Castener, Naireen Imtiaz'
SITENAME = 'CollectiwiseScience'
SITEURL = 'http://collectiwisescience.github.io'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'
IGNORE_FILES = ['.ipynb_checkpoints']
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#DISPLAY_CATEGORIES_ON_MENU = True
#DISPLAY_PAGES_ON_MENU = True






# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb.markup']

THEME = 'attila/'
IPYNB_USE_METACELL = True
IPYNB_SKIP_CSS = True



