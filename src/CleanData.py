#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np

df = pd.read_csv("PSQI_full.csv")

df.head()

df.dtypes

df.isnull()

df.isnull().sum()

df[df.psqi1.isnull()]

dfn = df.dropna(subset=['psqi1','psqi3'], how = 'all',inplace=True)

df.isnull().sum()

df[df.psqi5j.isnull()]

dfn = df['psqi5j'].fillna(value='0',inplace=True) 

df['psqi5j'].value_counts()

df.isnull().sum()

dfn = df.dropna(thresh=10, inplace=True)

df.isnull().sum()

dfn = df['psqi5h'].fillna(value='0.0',inplace=True) 

df.isnull().sum()

dfn = df.drop(df.index[[88]],inplace=True)

df.isnull().sum()

dfn = df['psqi4'].fillna(value='6.5',inplace=True) 

df.isnull().sum()

dfn = df['psqi5b'].fillna(value='3.0',inplace=True) 

df.isnull().sum()

dfn = df['psqi5d'].fillna(value='0.0',inplace=True) 

df.isnull().sum()

dfn = df['psqi2'].fillna(value='30',inplace=True) 

dfn = df['psqi5c'].fillna(value='3.0',inplace=True) 

dfn = df['psqi5e'].fillna(value='0.0',inplace=True) 

dfn = df['psqi5g'].fillna(value='0.0',inplace=True) 

dfn = df['psqi5i'].fillna(value='0.0',inplace=True) 

dfn = df['psqi8'].fillna(value='0.0',inplace=True) 

df.isnull().sum()

df.isnull().sum().any()

df = df.replace({
      'psqi2': '[A-Za-z]',
      'psqi4': '[A-Za-z]',
},'',regex=True)

df.replace(['midnight','between','MIDNIGHT'],['00:00:00','','00:00:00'])

df.shape

df.psqi1 = pd.to_datetime(df.psqi1, errors ='coerce') 

df.psqi3 = pd.to_datetime(df.psqi3, errors ='coerce') 

df.isnull().sum()

df['psqi1'] = df['psqi1'].fillna(method='ffill')

df['psqi3'] = df['psqi3'].fillna(method='ffill')

df.drop(df.index[[42]],inplace=True)

df.drop(df.index[[4]],inplace=True)

df = df.replace({
      'psqi2': '[A-Za-z-]',
      'psqi4': '[A-Za-z-]',
},'',regex=True)

df.drop(df.index[[332]])

df.head(100)

df.shape

df['psqi4'].replace(
    to_replace=['0.302083333', '6:45:00','8/9/2016','7/8/2016','5/6/2016','6/8/2017'],
    value='5.5',
    inplace=True
)

df.to_csv('cleanedData.csv', sep='\t')




