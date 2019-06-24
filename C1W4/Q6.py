# -*- coding: utf-8 -*-
"""
Created on Sun May 26 17:54:13 2019

@author: Shibo
"""

import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
df1 = df
begin = '2008q2'
ending = '2009q4'
low = '2009q2'
house4=pd.DataFrame()    

house4["ratio"]=house["2008Q2"]/house["2009Q2"]
house4=house4.dropna()
df1=df1.set_index(["State","RegionName"])
df1["uni"]=1
new=pd.merge(df1,house4,how="right",left_index=True,right_index=True)
new=new.fillna(0)
uniyes=new["ratio"][new["uni"]==1]
unino=new["ratio"][new["uni"]==0]
statistic,pvalue = tuple(ttest_ind(uniyes,unino))
if pvalue < 0.01:
    different = True
else:
    different = False
if float(np.nanmean(uniyes)) < float(np.nanmean(unino)):
    better="university town"
else:
    better="non-university town"