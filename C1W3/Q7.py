# -*- coding: utf-8 -*-
"""
Created on Tue May 14 13:18:53 2019

@author: Shibo
"""

import pandas as pd
import numpy as np
top15=answer_one()
top15["ratio"]=top15["Self-citations"]/top15["Citations"]
value7=top15["ratio"].sort_values(ascending=False).iloc[0]
country7=top15[top15["ratio"]==value7].iloc[0].name
def answer_seven():
    return (country7,value7)
answer_seven()