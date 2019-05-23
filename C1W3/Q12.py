# -*- coding: utf-8 -*-
"""
Created on Thu May 16 12:24:08 2019

@author: Shibo
"""

import pandas as pd
import numpy as np
ContinentDict = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
ans12=answer_one()
for i in range(len(ans12)):
    country12=ans12.iloc[i].name
    ans12.loc[country12,"Continent"]=ContinentDict[country12]
bin=pd.cut(ans12["% Renewable"],5)

def answer_twelve():
    Top15 = answer_one()
    return ans12.groupby(by=["Continent",bin]).size()