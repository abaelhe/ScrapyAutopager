# -*- coding: utf-8 -*-
from __future__ import absolute_import
import parsel
from autopager.htmlutils import get_links, get_xseq_yseq, get_link_text


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


def test_get_link_text():
    sel = parsel.Selector(u"<html><a>hello</a></html>")
    assert get_link_text(sel.css('a')[0]) == 'hello'

    sel = parsel.Selector(u"<html><a><span>hello</span></a></html>")
    assert get_link_text(sel.css('a')[0]) == 'hello'

    sel = parsel.Selector(u"<html><a><img alt='foo'/></a></html>")
    assert get_link_text(sel.css('a')[0]) == 'foo'

    sel = parsel.Selector(u'<a><span class="fa fa-arrow-left"></span> Newer Articles</a>')
    assert get_link_text(sel.css('a')[0]) == ' Newer Articles'
