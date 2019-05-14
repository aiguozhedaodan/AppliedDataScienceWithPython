# -*- coding: utf-8 -*-
"""
Created on Tue May 14 00:45:36 2019

@author: Shibo
"""

import pandas as pd
import numpy as np
top15=answer_one()
diliu=avgGDP.index[-6]
liu=top15.loc[diliu,'2006':'2015']
def answer_four():
    # return liu.max()-liu.min() This is wrong
    return liu['2015']-liu['2006']
answer_four()