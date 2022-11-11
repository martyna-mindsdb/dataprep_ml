import unittest
import pandas as pd

from type_infer.infer import infer_types

from data_insights.base import StatisticalAnalysis
from data_insights.insights import statistical_analysis


class TestInsights(unittest.TestCase):
    def test_0_hdi(self):
        df = pd.read_csv("tests/data/hdi.csv")
        inferred_types = infer_types(df, pct_invalid=0)
        args = {'target': 'Development Index'}
        sa = statistical_analysis(data=df,
                                  dtypes=inferred_types.dtypes,
                                  args=args)

        self.assertTrue(sa, isinstance(sa, StatisticalAnalysis))  # TODO: better asserts
