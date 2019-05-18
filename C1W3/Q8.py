# -*- coding: utf-8 -*-
"""
Created on Tue May 14 13:18:53 2019

@author: Shibo
"""

import pandas as pd
import numpy as np
top15=answer_one()
top15["population"]=top15["Energy Supply"]/top15["Energy Supply per Capita"]
value8=top15["population"].sort_values(ascending=False).iloc[2]
country8=top15[top15["population"]==value8].iloc[0].name
def answer_eight():
    return country8
answer_eight()