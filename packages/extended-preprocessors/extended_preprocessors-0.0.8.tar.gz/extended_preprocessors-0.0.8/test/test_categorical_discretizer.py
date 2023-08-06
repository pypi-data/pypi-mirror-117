import numpy as np

from extended_preprocessors.categorical_discretizer import CategoricalFeatureDiscretizer


def test_all_categories_covered():

    cats = np.array([1, 1, 1, 2, 2, 2, 3, 3, 3]).reshape((-1, 1))
    y = np.array([1, 1, 1, 2, 2, 2, 3, 3, 3])
    cfd = CategoricalFeatureDiscretizer()
    bins_map = cfd._make_bins_map(cats, y)
    expected = sorted(list(np.unique(cats).flatten()))
    actual = sorted(list(bins_map.keys()))
    assert expected == actual
