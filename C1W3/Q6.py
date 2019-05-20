# -*- coding: utf-8 -*-
"""
Created on Tue May 14 13:18:53 2019

@author: Shibo
"""

import pandas as pd
import numpy as np
top15=answer_one()
value6=top15["% Renewable"].sort_values(ascending=False).iloc[0]
country6=top15[top15["% Renewable"]==value6].iloc[0].name
def answer_six():
    return (country,value)
answer_six()