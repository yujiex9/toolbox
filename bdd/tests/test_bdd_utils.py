import pandas as pd
from pandas.testing import assert_frame_equal

from bdd.utils import gherkin_table_to_df


def test_gherkin_table_df_conversion():
    fruit_inventory = {
        'apple': 10,
        'banana': 15,
        'grape': 6,
        'orange': 11,
    }
    fruit_inventory_df = pd.DataFrame(fruit_inventory.items(), columns=['type', 'quantity'])
    
    fruit_inventory_text = """
    | type   | quantity |
    | apple  | 10       |
    | banana | 15       |
    | grape  | 6        |
    | orange | 11       |
    """
    df_  = gherkin_table_to_df(fruit_inventory_text)
    
    assert_frame_equal(fruit_inventory_df, df_)
