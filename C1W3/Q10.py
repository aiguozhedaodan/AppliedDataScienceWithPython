# -*- coding: utf-8 -*-
"""
Created on Tue May 14 13:18:53 2019

@author: Shibo
"""

import pandas as pd
import numpy as np
top15=answer_one().sort_values("% Renewable",ascending=True)
median=top15["% Renewable"].iloc[7]
for i in range(len(top15)):
    country=top15.iloc[i,].name
    if top15.iloc[i]["% Renewable"]>=median:
        top15.loc[country,"HighRenew"]=1
    else:
        top15.loc[country,"HighRenew"]=0
def answer_ten():
    return top15["HighRenew"].astype('int')
answer_ten()
