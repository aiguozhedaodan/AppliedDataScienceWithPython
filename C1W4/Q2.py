# -*- coding: utf-8 -*-
"""
Created on Sun May 26 12:30:03 2019

@author: Shibo
"""

import pandas as pd
import numpy as np
data2 = pd.read_excel("gdplev.xls",skiprows=7)
gdp=data2.iloc[212:,[4,6]]
n=0
for n in range(len(gdp)-2):
    n0=gdp.iloc[n,1]
    n1=gdp.iloc[n+1,1]
    n2=gdp.iloc[n+2,1]
    
    if n1<n0 and n2<n1:
        time=gdp.iloc[n+1,0]
        value=n
        break

