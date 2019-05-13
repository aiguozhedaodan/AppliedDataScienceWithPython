# -*- coding: utf-8 -*-
"""
Created on Mon May 13 17:17:25 2019

@author: Shibo
"""
import pandas as pd
import numpy as np

def answer_one(): 
    df = pd.read_excel('Energy Indicators.xls',skiprows=17,skipfooter=38)
    df=df.drop(["Unnamed: 0","Unnamed: 1"],axis=1)
    ## TypeError: drop() got an unexpected keyword argument 'columns' so changed
    df.columns=["Country","Energy Supply","Energy Supply per Capita","% Renewable"]
    df=df.replace(to_replace="...", value=np.NaN)
    df=df.replace(to_replace=[r'\d',r' \([a-zA-Z ]*\)'], value=r'', regex=True)
    df=df.replace(to_replace=["Republic of Korea","United States of America","United Kingdom of Great Britain and Northern Ireland","China, Hong Kong Special Administrative Region"], value=["South Korea","United States","United Kingdom","Hong Kong"])
    # Another regex is ' \(([^)]+)\)' and a perfect website is regex101.com
    df["Energy Supply"]=df["Energy Supply"]*1000000
    energy=df

    GDP=pd.read_csv("world_bank.csv",skiprows=4)
    GDP=GDP.replace(to_replace=["Korea, Rep.","Iran, Islamic Rep.","Hong Kong SAR, China"], value=["South Korea","Iran","Hong Kong"])

    ScimEn=pd.read_excel('scimagojr-3.xlsx')
    ScimEn=ScimEn[ScimEn["Rank"]<=15]

    GDP=GDP[["Country Name",'2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]
    new=pd.merge(ScimEn,energy,how="inner",on="Country")
    new=pd.merge(new,GDP,how="inner",left_on="Country",right_on="Country Name")
    return new.set_index("Country").drop("Country Name",axis=1)
answer_one()