# -*- coding: utf-8 -*-
from __future__ import absolute_import

import tldextract


def get_domain(url):
    """
    >>> get_domain('example.org')
    'example'
    >>> get_domain('foo.example.co.uk')
    'example'
    """
    return tldextract.extract(url).domain
