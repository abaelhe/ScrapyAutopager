# -*- coding: utf-8 -*-
from __future__ import absolute_import  
import parsel


def _get_links(sel):
    for el in sel:
        links_parent = el.xpath('ancestor::a')
        if links_parent:
            for link in links_parent:
                yield link
        else:
            for link in el.css('a'):
                yield link


def get_links(sel):
    """
    Return ``<a>`` elements for a selector.

    If selection is inside <a> element, this parent <a> element is returned.
    If selection is <a> element, it is returned.
    If selection has <a> children, they are returned.
    """
    return parsel.SelectorList(_get_links(sel))


def get_xseq_yseq(html, selectors, validate=True):
    """
    Extract links from ``html`` and assign each link a class label
    if it matches one of the ``selectors`` or "O" if it matches none of them.
    Only ``<a>`` elements with ``href`` attributes are returned.

    ``selectors`` is a ``{label: selector}`` dict.

    When ``validate`` is True this function checks that each selector
    returns non-empty result, and that results don't overlap; in case of
    errors it prints error messages.
    """
    sel = parsel.Selector(html)
    links = sel.xpath('.//a[@href]')
    links_extracted = links.extract()
    classes = ["O"] * len(links)

    for label, selector in selectors.items():
        if not selector:
            continue
        sel_links = set(get_links(sel.css(selector)).extract())
        if validate and not sel_links:
            print("error: links not found", label, selector)
        matched_links = set()
        for idx, link in enumerate(links_extracted):
            if link in sel_links:
                if validate and classes[idx] != 'O':
                    print("warning: link is classified in more than 1 classes",
                          link, label)
                matched_links.add(link)
                classes[idx] = label
        if validate and matched_links != sel_links:
            print("Not all links are matched", sel_links - matched_links)

    return links, classes


def get_link_text(link):
    """
    Return text of <a> element: either its string contents or the 'alt'
    of <img> tags inside.
    """
    txt = ' '.join(link.xpath('string()').extract())
    if not txt:
        txt = ' '.join(link.xpath('.//img/@alt').extract())
    return txt
