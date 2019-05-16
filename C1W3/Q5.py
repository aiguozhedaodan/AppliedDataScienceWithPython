# -*- coding: utf-8 -*-
"""
Created on Tue May 14 13:18:53 2019

@author: Shibo
"""

import pandas as pd
import numpy as np
top15=answer_one()
def answer_five():
    return top15["Energy Supply per Capita"].mean()
answer_five()