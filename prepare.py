import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import acquire

df = pd.read_csv('big_df.csv', index_col=0)
ogd = pd.read_csv('opsd_germany_daily.csv', index_col=0)

def prep_store():
    # acquires store data from local csv (see acquire.py)
    df = pd.read_csv('big_df.csv', index_col=0)
    # sets sale_date to a datetime datatype
    df.sale_date = pd.to_datetime(df.sale_date)
    # sets the index to the date for each observation
    df = df.set_index("sale_date").sort_index()
    # add month and day_of_week columns to the dataframe
    df['month'] = df.index.month
    df['day_of_week'] = df.index.day_name()
    # add sales_total column by multiplying sale_amount and item_price
    df['sales_total'] = df.sale_amount * df.item_price
    return df

def plot_store_dist():
    df[['sale_amount', 'item_price']].hist()

def prep_ogd():
    # acquires opsd_german_daily data from local csv (see acquire.py)
    ogd = pd.read_csv('opsd_germany_daily.csv', index_col=0)
    # sets Date to a datetime datatype
    ogd.Date = pd.to_datetime(ogd.Date)
    # sets the index to the date for each observation
    ogd = ogd.set_index('Date').sort_index()
    # add month and year columns to the dataframe
    ogd['month'] = ogd.index.month
    ogd['year'] = ogd.index.year
    # Fill missing values:
    # change Solar and Wind Columns to 0
    ogd[['Solar', 'Wind']] = ogd[['Solar', 'Wind']].fillna(0)
    # add the Wind and Solar Columns together to get actual values
    ogd['Wind+Solar'] = ogd.Wind + ogd.Solar
    return ogd

def plot_ogd_dist():
    ogd.hist()
    plt.tight_layout()
