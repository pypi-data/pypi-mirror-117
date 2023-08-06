import numpy as np
import pytest
from extended_preprocessors.feature_discretizer import FeatureDiscretizer


@pytest.fixture()
def make_y():
    ones = [np.ones(5) for i in range(5)]
    y_vals = np.random.choice(np.arange(1, 1000), size=5, replace=True)
    result = np.hstack([o * y for o, y in zip(ones, y_vals)])
    return result

@pytest.fixture()
def make_bins():
    return np.hstack([
        np.ones(5) * 0,
        np.ones(5) * 1,
        np.ones(5) * 2,
        np.ones(5) * 3,
        np.ones(5) * 4
    ])

@pytest.mark.parametrize("max_bins, data, expected",[
    (10, np.arange(100), 10),
    (10, np.arange(5), 5)
])
def test_define_n_bins(max_bins, data, expected):
    fd = FeatureDiscretizer(max_bins=max_bins)
    calc_max_bins = fd._define_n_bins(data)
    assert calc_max_bins == expected


def test_make_bins_map_ordinal(make_y, make_bins):


    bins = make_bins
    y = make_y
    unique_y, y_index = np.unique(y, return_index=True)
    sort_key = lambda x: {v: i for v, i in zip(unique_y, y_index)}[x]
    sorted_y = sorted(unique_y, key=sort_key)

    bin_value_map = {i: v for i, v in enumerate(sorted_y)}
    values_order_map = {v: i+1 for i, v in enumerate(unique_y)}
    expected_bin_map = {bin_v: values_order_map.get(value_v) for bin_v, value_v in bin_value_map.items()}

    fd = FeatureDiscretizer(max_bins=5)
    result = fd._make_bins_map(bins, y)

    assert result == expected_bin_map


def test_make_bins_map_mean_encoded(make_y, make_bins):

    bins = make_bins
    y = make_y
    unique_y, y_index = np.unique(y, return_index=True)
    bin_value_map = {b: v for b, v in zip(bins, y)}
    fd = FeatureDiscretizer(max_bins=5)
    result = fd._make_bins_map(bins, y, encode_with_expected=True)
    print(result)
    assert result == bin_value_map

