#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# from __future__ import unicode_literals
import os

AUTHOR = 'Cheyne Homberger'
SITENAME = 'Cheyne Homberger'
SITEURL = 'http://cheynehomberger.com'

PATH = 'content'
THEME = 'myflasky'

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
GOOGLE_ANALYTICS_ACCOUNT = 'UA-45764157-1'
MAIL_USERNAME = 'cheyne.homberger'
MAIL_HOST = 'gmail.com'
GITHUB_URL = 'http://github.com/cheyneh'
LINKEDIN_URL = 'https://www.linkedin.com/pub/cheyne-homberger/63/647/883'
GOOGLE_SCHOLAR_URL = 'https://scholar.google.com/citations?user=joyBnGMAAAAJ&hl=en'
RESEARCHGATE_URL = 'https://www.researchgate.net/profile/Cheyne_Homberger'
ACADEMIA_URL = None
ARXIV_URL = 'http://arxiv.org/a/homberger_c_1.html'
MENDELEY_URL = None


# # set private variables?
# cur_dir = os.path.dirname( os.path.realpath(__file__) )
# with open( os.path.join(cur_dir, 'private_vars.py') ) as f:
#     text = f.read()
#     exec(text)


DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
