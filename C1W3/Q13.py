# -*- coding: utf-8 -*-
"""
Created on Thu May 16 13:42:06 2019

@author: Shibo
"""
import pandas as pd
import numpy as np
ans=answer_one()
ans["PopEst"]=ans["Energy Supply"]/ans["Energy Supply per Capita"]
def answer_thirteen():
    return ans['PopEst'].apply(lambda x:'{:,}'.format(x))
# Another way
#i=0
#for p in ans['PopEst']:
#    c=ans.iloc[i].name
#    p='{:,}'.format(p)
#    ans.loc[c,'PopEst']=p
#    i=i+1

#https://docs.python.org/3/library/string.html#format-string-syntax