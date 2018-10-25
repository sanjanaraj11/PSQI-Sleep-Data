#!/usr/bin/env python
# coding: utf-8

# In[488]:


import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import json
import sys

#Command line arguements
inputFile = sys.argv[1];
outputPath = sys.argv[2]; #if you want the user to explicitly specify the output path

df = pd.read_csv(inputFile)


# # Pandas Dataframe to read the csv file and store it
#df = pd.read_csv("cleanedDatas.csv")

# # Copy the contents of 'psqi9' into a new column 'comp1'

df['comp1'] = df['psqi9']

# # Function to calculate the subscore 2q

#The function witll check the 'psqi2' values and using conditional ifs will return the assigned score. The new column will be of int type for further calculations

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


# # Copy 'psqi5a' into a new column 'sub5a'

df['sub5a'] = df['psqi5a']

df.head()

# # Compute the sum of 'sub5a' and 'sub2q' and store it in 'sub2'

df['sub2'] = df['sub5a'] + df['sub2q']

df.head()


# # Function to compute component 2

#The function witll read 'sub2' values with conditional ifs and return the assigned score and storing the result in a new column 'comp2'

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

# # Function to compute component 3

#Function will read 'psqi4' with conditional ifs and return the assigned score and store it in a new column 'comp3'

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


# # Convert 'psqi1' and 'psqi3' to datetime object

df['psqi1'] = pd.to_datetime(df['psqi1'],format ='%Y-%m-%d %H:%M:%S')

df['psqi3'] = pd.to_datetime(df['psqi3'],format ='%Y-%m-%d %H:%M:%S')


# # Function to compute the time column by calculating the difference in timedelta

from datetime import datetime
df['time'] = (24-(pd.to_datetime(df['psqi1']) - pd.to_datetime(df['psqi3'])) / np.timedelta64(1,'h'))


# # Function to compute efficiency using 'psqi4' and 'time'

def sub4(row3):
    effi = (row3['psqi4']/row3['time']) * 100
    return effi 
df['sub4'] = df.apply(sub4, axis=1).astype(int)
df['sub4'].astype(int)

df.head()


# # Function to compute 'comp4' and return the assigned score 

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


# # Function to compute 'sub5' by summation of all 5b-j columns

def sub5(row5):
    sum = row5['psqi5b'] +row5['psqi5c']+row5['psqi5d']+row5['psqi5e']+row5['psqi5f']+row5['psqi5g']+row5['psqi5h']+row5['psqi5i']+row5['psqi5j']
    return sum 
df['sub5'] = df.apply(sub5, axis=1)   


# # Function to compute 'comp5' based on 'sub5'

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


# # Copy 'psqi6' to a new column 'comp6'

df['comp6'] = df['psqi6']

# # Copy 'psqi8' to a new column 'comp7'

df['comp7'] = df['psqi8']

df.shape


# # Compute Global PSQI by summation of all components

df['GlobalPSQI'] = df['comp1'] + df['comp2']  + df['comp4'] + df['comp3'] + df['comp5'] + df['comp6'] + df['comp7']

df.plot(x='GlobalPSQI', y='comp5', kind = 'bar')

df.plot(y='comp4', kind = 'bar')


# # Plot a scatter graph for Global PSQI and sleep efficiency

df.plot(x='comp4',y='GlobalPSQI', linestyle = 'none', marker = 'o')

df.plot(x='comp5',y='GlobalPSQI', linestyle = 'none', marker = 'o')

df.plot(y='GlobalPSQI', x = 'comp5', kind = 'bar')


#Command line arguements
df.to_csv(outputPath, sep='\t')

#df.to_csv('cleanedDatas.csv', sep='\t') 
