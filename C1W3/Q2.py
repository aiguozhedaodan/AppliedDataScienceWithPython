# -*- coding: utf-8 -*-
"""
Created on Mon May 13 17:27:03 2019

@author: Shibo
"""

import pandas as pd
import numpy as np
def answer_two():
    df = pd.read_excel('Energy Indicators.xls',skiprows=17,skipfooter=38)
    df=df.drop(["Unnamed: 0","Unnamed: 1"],axis=1)
    df.columns=["Country","Energy Supply","Energy Supply per Capita","% Renewable"]
    df=df.replace(to_replace="...", value=np.NaN)
    df=df.replace(to_replace=[r'\d',r' \([a-zA-Z ]*\)'], value=r'', regex=True)
    df=df.replace(to_replace=["Republic of Korea","United States of America","United Kingdom of Great Britain and Northern Ireland","China, Hong Kong Special Administrative Region"], value=["South Korea","United States","United Kingdom","Hong Kong"])
    energy=df
    ScimEn=pd.read_excel('scimagojr-3.xlsx')
    GDP=pd.read_csv("world_bank.csv",skiprows=4)
    GDP=GDP.replace(to_replace=["Korea, Rep.","Iran, Islamic Rep.","Hong Kong SAR, China"], value=["South Korea","Iran","Hong Kong"])
    scienergy=pd.merge(ScimEn,energy,how="inner",on="Country")
    scigdp=pd.merge(ScimEn,GDP,how="inner",left_on="Country",right_on="Country Name")
    energygdp=pd.merge(energy,GDP,how="inner",left_on="Country",right_on="Country Name")
    all=pd.merge(scienergy,energygdp,how="inner",on="Country")
    #lose=len(energy)+len(ScimEn)+len(GDP)-len(scienergy)-len(scigdp)-len(energygdp)+len(all) This is a wrong way
    lose2=len(pd.merge(pd.merge(ScimEn,energy,on='Country',how ='outer'),GDP,left_on='Country',right_on='Country Name',how ='outer'))-len(all)
    return int(lose2)