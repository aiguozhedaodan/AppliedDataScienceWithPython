# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:51:31 2019

@author: Shibo
"""
import pandas as pd
import numpy as np
ContinentDict = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
top15=answer_one()
i=0
top15["population"]=top15["Energy Supply"]/top15["Energy Supply per Capita"]
a=pd.DataFrame(columns=["c","p"])
for key,value in ContinentDict.items():
    a.loc[i,"c"]=value
    a.loc[i,"p"]=top15.loc[key,"population"]
    i=i+1
ans=pd.DataFrame({"size":[a[a["c"]=='Asia']["c"].count(),a[a["c"]=='Australia']["c"].count(),a[a["c"]=='Europe']["c"].count(),a[a["c"]=='North America']["c"].count(),a[a["c"]=='South America']["c"].count()],"sum":[a[a["c"]=='Asia']["p"].sum(),a[a["c"]=='Australia']["p"].sum(),a[a["c"]=='Europe']["p"].sum(),a[a["c"]=='North America']["p"].sum(),a[a["c"]=='South America']["p"].sum()],"mean":[a[a["c"]=='Asia']["p"].mean(),a[a["c"]=='Australia']["p"].mean(),a[a["c"]=='Europe']["p"].mean(),a[a["c"]=='North America']["p"].mean(),a[a["c"]=='South America']["p"].mean()],"std":[a[a["c"]=='Asia']["p"].std(),a[a["c"]=='Australia']["p"].std(),a[a["c"]=='Europe']["p"].std(),a[a["c"]=='North America']["p"].std(),a[a["c"]=='South America']["p"].std()]},index=['Asia', 'Australia', 'Europe', 'North America', 'South America']).astype('float')
def answer_eleven():
    return ans