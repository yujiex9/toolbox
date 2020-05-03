import re
from io import StringIO

import numpy as np
import pandas as pd
from pandas.errors import EmptyDataError


def gherkin_table_to_df(text):
    try:
        df = pd.read_table(StringIO(text), sep='\s*\|\s*', engine='python', nrows=1)
    except EmptyDataError:
        return pd.DataFrame()
    
    dates_cols = [col for col in df.columns if 'date' in col]
    na_values = ['', 'None', np.nan]
    df = pd.read_table(StringIO(text),
                       sep='\s*\|\s*',
                       engine='python',
                       na_values=na_values,
                       parse_dates=dates_cols,
                       infer_datetime_format=True)
    df = df[df.columns[1:-1]]
    
    return df


def df_to_gherkin_table(df, rule='right'):
    if not isinstance(df, pd.DataFrame):
        return ''
    
    def gen_aligned_row(cell_id, cell_content, rule):
        spaces = ' ' * (cell_maxlen_mapping[cell_id] - len(cell_content))
        if rule == 'right':
            aligned_row = f' {spaces}{cell_content} '
        elif rule == 'left':
            aligned_row = f' {cell_content}{spaces} '
        elif rule == 'centre' or rule == 'center':
            no_spaces = len(spaces)
            left = right = no_spaces // 2
            if left + right < no_spaces:
                right += 1
            left = ' ' * left
            right = ' ' * right
            aligned_row = f' {left}{cell_content}{right} '
        else:
            msg = 'Valid alignment rule is either left, right or centre(center), but {rule} is given'
            raise ValueError(msg)
        return aligned_row
    
    def gen_processed_row(df_row):
        row_content = [gen_aligned_row(cell_id, str(cell), rule)
                       for cell_id, cell in enumerate(df_row)]
        row = re.sub('^|$', '|', '|'.join(row_content))
        return row
    
    cols = df.columns.tolist()
    no_rows = len(df.index)

    cell_maxlen_mapping = {}
    for col_id, col in enumerate(cols):
        cell_maxlen_mapping[col_id] = max(len(str(item)) for item in df[col].tolist() + [col])

    matrix_content = [gen_processed_row(cols)]
    matrix_content += [gen_processed_row(df.iloc[i, :]) for i in range(no_rows)]

    return '\n'.join(matrix_content)
