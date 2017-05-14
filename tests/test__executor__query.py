from __future__ import print_function, division, absolute_import

from framequery.executor import query

import pandas as pd
import pandas.util.testing as pdt


scope = dict(
    example=pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]}),
)


def test_example():
    actual = query('select * from example', scope=scope)
    expected = scope['example'].copy()

    pdt.assert_frame_equal(actual, expected, check_dtype=False)


def test_example2():
    actual = query('select * from example order by a desc', scope=scope)
    expected = scope['example'].copy().sort_values('a', ascending=False)

    pdt.assert_frame_equal(actual, expected, check_dtype=False)


def test_example3():
    actual = query('select a + b as c from example', scope=scope)
    expected = scope['example'].copy()
    expected = pd.DataFrame({'c': expected['a'] + expected['b']})

    pdt.assert_frame_equal(actual, expected, check_dtype=False)
