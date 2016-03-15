# -*- coding: utf-8 -*-
from __future__ import absolute_import

from autopager.utils import get_domain


def get_annotation_folds(urls, n_folds):
    """
    Return (train_indices, test_indices) folds iterator.
    It is guaranteed pages from the same website can't be both in
    train and test parts.

    We must be careful when splitting the dataset into training and
    evaluation parts: pages from the same domain should be in the same
    "bin". There could be several pages from the same domain, and these
    pages may have duplicate or similar link patterns
    (e.g. a particular CSS class for paginator links).
    If we put one such page in a training dataset and another in
    an evaluation dataset then the metrics will be too optimistic,
    and they can make us to choose wrong features/models. It means
    train_test_split from scikit-learn shouldn't be used here
    """
    from sklearn.cross_validation import LabelKFold
    return LabelKFold(
        labels=[get_domain(url) for url in urls],
        n_folds=n_folds
    )
