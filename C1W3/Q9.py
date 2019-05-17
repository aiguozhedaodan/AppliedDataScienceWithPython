# -*- coding: utf-8 -*-
"""
Created on Tue May 14 13:18:53 2019

@author: Shibo
"""

import pandas as pd
import numpy as np
top15=answer_one()
top15["PopEst"]=top15["Energy Supply"]/top15["Energy Supply per Capita"]
top15['Citable docs per Capita'] = top15['Citable documents'] / top15['PopEst']
test=top15[['Citable docs per Capita',"Energy Supply per Capita"]]
ans=test.corr(method='pearson').iloc[0,1]
def answer_nine():
    return ans
answer_nine()
