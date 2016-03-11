# -*- coding: utf-8 -*-
from __future__ import absolute_import
import parsel
from autopager.htmlutils import get_links, get_xseq_yseq


def test_get_links():
    sel = parsel.Selector(u"""
    <html>
        <div><a id=1></a></div>
        <a id=2><div></div></a>
        <a id=3></a>
    </html>
    """)
    assert get_links(sel.css('div')).xpath("@id").extract() == ['1', '2']
    assert get_links(sel.css('a#2')).xpath("@id").extract() == ['2']


def test_xseq_yseq():
    """
    Extract links from ``html`` and assign each link a class label
    if it matches one of the ``selectors`` or "O" if it matches none of them.
    Only ``<a>`` elements with ``href`` attributes are returned.

    ``selectors`` is a ``{label: selector}`` dict.

    When ``validate`` is True this function checks that each selector
    returns non-empty result, and that results don't overlap; in case of
    errors it prints error messages.
    """

    html = u"""
    <html>
        <div><a href="/" id=1></a></div>
        <a href="/" id=2><div></div></a>
        <a href="/" id=3></a>
        <a id=4></a>
    </html>
    """
    links, classes = get_xseq_yseq(html, {"SECOND": "a#2", "INVALID": ""})
    assert len(links) == 3
    assert classes == ['O', 'SECOND', 'O']
