#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import sys
get_ipython().run_line_magic('matplotlib', 'inline')

#df = pd.read_csv("cleanedDatas.csv")

inputFile = sys.argv[1];
outputPath = sys.argv[2]; #if you want the user to explicitly specify the output path

df = pd.read_csv(inputFile)

df['comp1'] = df['psqi9']

df.head()
def subscoreq2(row):
    if row['psqi2']<=15:
        return 0
    if row['psqi2'] in range(16,31):
        return 1
    if row['psqi2'] in range(31,61):
        return 2
    if row['psqi2']>=60:
        return 3
df['sub2q'] = df.apply(subscoreq2, axis=1)      
df['sub2q'].astype(int)

df['sub5a'] = df['psqi5a']

df.head()

df['sub2'] = df['sub5a'] + df['sub2q']

df.head()

def component2(row1):
    if row1['sub2']==0:
        return 0
    if row1['sub2'] in range(1,3):
        return 1
    if row1['sub2'] in range(3,5):
        return 2
    if row1['sub2'] in range(5,7):
        return 3
df['comp2'] = df.apply(component2, axis=1)      
df['comp2'].astype(int)
df.head()
def component3(row2):
    if row2['psqi4']>7:
        return 0
    if row2['psqi4'] in range(6,8):
        return 1
    if row2['psqi4'] in range(5,7):
        return 2
    if row2['psqi4']<5:
        return 3
    if row2['psqi4']==5.5:
        return 2
    if row2['psqi4']==6.5:
        return 1
    if row2['psqi4']==5.56:
        return 2
    if row2['psqi4']==5.75:
        return 2
df['comp3'] = df.apply(component3, axis=1)      
df['psqi1'] = pd.to_datetime(df['psqi1'],format ='%Y-%m-%d %H:%M:%S')

df['psqi3'] = pd.to_datetime(df['psqi3'],format ='%Y-%m-%d %H:%M:%S')

from datetime import datetime
df['time'] = (24-(pd.to_datetime(df['psqi1']) - pd.to_datetime(df['psqi3'])) / np.timedelta64(1,'h'))

def sub4(row3):
    effi = (row3['psqi4']/row3['time']) * 100
    return effi 
df['sub4'] = df.apply(sub4, axis=1).astype(int)

def component4(row4):
    if row4['sub4']>=85:
        return 0
    if row4['sub4'] in range(75,85):
        return 1
    if row4['sub4'] in range(65,75):
        return 2
    if row4['sub4']<65:
        return 3
df['comp4'] = df.apply(component4, axis=1)   

def sub5(row5):
    sum = row5['psqi5b'] +row5['psqi5c']+row5['psqi5d']+row5['psqi5e']+row5['psqi5f']+row5['psqi5g']+row5['psqi5h']+row5['psqi5i']+row5['psqi5j']
    return sum 
df['sub5'] = df.apply(sub5, axis=1)   

def component5(row6):
    if row6['sub5']==0:
        return 0
    if row6['sub5'] in range(1,10):
        return 1
    if row6['sub5'] in range(10,19):
        return 2
    if row6['sub5'] in range(19,28):
        return 3
df['comp5'] = df.apply(component5, axis=1) 

df['comp6'] = df['psqi6']

df['comp7'] = df['psqi8']

df.shape

df['GlobalPSQI'] = df['comp1'] + df['comp2']  + df['comp4'] + df['comp3'] + df['comp5'] + df['comp6'] + df['comp7']

df.plot(x='comp4',y='GlobalPSQI', linestyle = 'none', marker = 'o')

df.to_csv(outputPath, sep='\t')
