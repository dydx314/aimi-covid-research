from typing import List

import numpy as np
import pandas as pd

def create_lagged_features(df: pd.DataFrame, lag_periods: List[int]):
    unpivoted = df.melt(id_vars=['Country', 'GDP per capita'], var_name='reported_date', value_name='cases')
    unpivoted.reported_date = unpivoted.reported_date.astype('datetime64')

    joined = unpivoted
    for period in lag_periods:

        lagged = unpivoted[['Country', 'cases']].groupby(['Country']).\
            transform(lambda x: x.shift(periods=period, fill_value=0))
        joined = joined.join(lagged, lsuffix='', rsuffix=f'_{period}')

    return joined
