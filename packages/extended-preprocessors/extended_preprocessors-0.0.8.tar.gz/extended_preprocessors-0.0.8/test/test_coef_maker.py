import numpy as np
import pandas as pd
import pytest

from extended_preprocessors.coef_maker import CoefficientMaker

@pytest.fixture()
def make_dataset():
    return pd.DataFrame(np.random.randint(0, 100, size=(10, 5))
                        , columns = [f'col_{i}' for i in range(1, 6)])

@pytest.mark.parametrize("coef_cols, expected_cols",
                         [
                             (['col_1', 'col_2'], ['col_1_div_col_2']),
                             (['col_1', 'col_2', 'col_5']
                              , ['col_1_div_col_2', 'col_1_div_col_5', 'col_2_div_col_5']),
                             (['col_1']
                              , [])
                         ]
                         )
def test_columns_set(make_dataset, coef_cols, expected_cols):
    df = make_dataset
    cm = CoefficientMaker(coef_cols)
    transf_df = cm.transform(df)
    cols_after = [c for c in transf_df.columns if c not in df.columns]
    assert cols_after == expected_cols

def test_calculation(make_dataset):
    df = make_dataset
    cm = CoefficientMaker(['col_1', 'col_2'])
    transf_df = cm.transform(df)
    expected_col = df.col_1 / df.col_2
    assert (transf_df.col_1_div_col_2.fillna(0) == expected_col.fillna(0)).all()