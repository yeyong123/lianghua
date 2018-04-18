# coding:utf-8
# File Name: month_income.py
# Created Date: 2018-04-18 09:32:02
# Last modified: 2018-04-18 09:44:02
# Author: yeyong

import numpy as np
import pandas as pd
import itertools
from datetime import datetime
from scipy import stats as ss
from dateutil.parse import parse
import matplotlib.pyplot as plt
import seaborn as sn
sn.set_style('white')

def get_sw_ind_quotation():
    index_symbol = DataAPI.IndustryGet(industryVersion=u'SW', industryVersionCD=u'', industryLevel=u"1", isNew=u"1", field=u"",  pandas="1")["indexSymbol"].tolist()

    index_symbol = [str(item) + '.ZICN' for item in index_symbol]

    symbol_history_list = []
    for symbol in index_symbol:
        df_daily_industry_symbol = DataAPI.MktIdxdGet(beginDate='2018-1-1', endDate='2018-4-18', ticker=symbol[:6], field=u"ticker, tradeDate, closeIndex")
        symbol_history_list.append(df_daily_industry_symbol)

    df_daily_industry_symbol = pd.concat(df_daily_industry_symbol)
    df_daily_industry_unstack = df_daily_industry_symbol.set_index(["tradeDate", 'ticker']).unstack()['closeIndex']

    return df_daily_industry_unstack

df_daily_industry_unstack = get_sw_ind_quotation()
df_daily_industry_unstack.head()

    
