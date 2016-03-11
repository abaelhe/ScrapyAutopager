# -*- coding: utf-8 -*-
from __future__ import absolute_import
import os
import csv
import codecs

from autopager.htmlutils import get_xseq_yseq


DEFAULT_DATA_PATH = os.path.join(os.path.dirname(__file__), 'data')


class Storage(object):
    def __init__(self, path=DEFAULT_DATA_PATH):
        self.path = path

    def get_Xy(self):
        X, y = [], []
        for row in self.iter_records():
            html = self._load_html(row)
            selectors = {key: row[key]
                         for key in ['FIRST', 'LAST', 'NEXT', 'PREV', 'PAGE']}
            xseq, yseq = get_xseq_yseq(html, selectors, validate=True)
            X.append(xseq)
            y.append(yseq)
        return X, y

    def iter_records(self):
        info_path = os.path.join(self.path, 'data.csv')
        with codecs.open(info_path, encoding='utf8') as f:
            for row in csv.DictReader(f):
                if row['failed']:
                    continue
                yield row

    def _load_html(self, row):
        data_path = os.path.join(self.path, 'html')
        path = os.path.join(data_path, row['File Name'] + ".html")
        with codecs.open(path, encoding=row['Encoding']) as f:
            return f.read()


