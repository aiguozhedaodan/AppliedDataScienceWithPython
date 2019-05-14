# -*- coding: utf-8 -*-
"""
Created on Mon May 13 20:09:41 2019

@author: Shibo
"""

import pandas as pd
import numpy as np
top15=answer_one()
avgGDP=top15[['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']].mean(axis=1).sort_values(ascending=True)
def answer_three():
    return avgGDP
answer_three()