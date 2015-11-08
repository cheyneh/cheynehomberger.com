#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# from __future__ import unicode_literals
import os

AUTHOR = 'Cheyne Homberger'
SITENAME = 'Cheyne Homberger'
SITEURL = 'http://cheynehomberger.com'

PATH = 'content'
THEME = 'cheynes_theme'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

SECTIONS = [
        # ('About', 'index.html'),
        ('Papers', 'category/papers.html'),
        ('Talks', 'category/talks.html'),
        ('Teaching', 'category/teaching.html'),
        ]


# folders containing static files
STATIC_PATHS = ['images', 'pdfs']


# how to create the slug (the short name for each article)
SLUGIFY_SOURCE = 'basename'

# how to organize the urls
ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'


# Keep these at none to turn off feed stuff
FEED_ATOM = None
FEED_RSS = None
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# social media accounts --- setting these will create links in the footer
GOOGLE_ANALYTICS_ACCOUNT = None
MAIL_USERNAME = None
MAIL_HOST = None
GITHUB_URL = None
LINKEDIN_URL = None
GOOGLE_SCHOLAR_URL = None
RESEARCHGATE_URL = None
ACADEMIA_URL = None
ARXIV_URL = None
MENDELEY_URL = None

# set my values for each of the variables above
cur_dir = os.path.dirname( os.path.realpath(__file__) )
with open( os.path.join(cur_dir, 'private_vars.py') ) as f:
    text = f.read()
    exec(text)



DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
