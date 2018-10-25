#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import sys



# Command line arguements
inputFile = sys.argv[1];
outputPath = sys.argv[2]; #if you want the user to explicitly specify the output path

df = pd.read_csv(inputFile)
# # Pandas dataframe to read the csv file
#df = pd.read_csv("PSQI_full.csv")

df.head()

# # Checking the datatypes of each column

df.dtypes


# # Check to see if there are any missing values

df.isnull()

df.isnull().sum()


# # Check the first column 'psqi1' for missing values

df[df.psqi1.isnull()]


# # Drop the rows where both 'psqi1' and 'psqi3' are missing

dfn = df.dropna(subset=['psqi1','psqi3'], how = 'all',inplace=True)

df.isnull().sum()

df[df.psqi5j.isnull()]


# # Fill NaN with the most answered value in 'psqi5j' 

dfn = df['psqi5j'].fillna(value='0',inplace=True) 

df['psqi5j'].value_counts()

df.isnull().sum()


# # Drop all the rows with more than 9 missing values

dfn = df.dropna(thresh=10, inplace=True)

df.isnull().sum()


# # Fill the NaNs with the most answered value

dfn = df['psqi5h'].fillna(value='0.0',inplace=True) 

df.isnull().sum()

dfn = df.drop(df.index[[88]],inplace=True)

df.isnull().sum()


# # Fill NaN values in 'psqi4' with the most answered value

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


# # Use Regex to replace all the strings from 'psqi2' and 'psqi4'

df = df.replace({
      'psqi2': '[A-Za-z]',
      'psqi4': '[A-Za-z]',
},'',regex=True)

# # Use replace function to replace all the midnight into time[24HR]

df.replace(['midnight','between','MIDNIGHT'],['00:00:00','','00:00:00'])


# # Check to see the number of rows and columns after cleaning

df.shape

df.head()

# # Convert the object dtype to datetime for 'psqi1'

df.psqi1 = pd.to_datetime(df.psqi1, errors ='coerce') 

# # # Convert the object dtype to datetime for 'psqi3'

df.psqi3 = pd.to_datetime(df.psqi3, errors ='coerce') 

df.isnull().sum()


# # Forward Fill all the NaT values in 'psqi1'

df['psqi1'] = df['psqi1'].fillna(method='ffill')

df['psqi3'] = df['psqi3'].fillna(method='ffill')


df.head(20)

df.isnull().sum()

df.drop(df.index[[42]],inplace=True)

df.drop(df.index[[4]],inplace=True)

df = df.replace({
      'psqi2': '[A-Za-z-]',
      'psqi4': '[A-Za-z-]',
},'',regex=True)

# # Recheck the number of rows and columns after cleaning.

df.shape


# # Replace the dirty data with a rand value

df['psqi4'].replace(
    to_replace=['0.302083333', '6:45:00','8/9/2016','7/8/2016','5/6/2016','6/8/2017'],
    value='5.5',
    inplace=True
)


# # Save the cleaned data in a csv file
#df.to_csv('cleanedData.csv', sep='\t')
#Command line arguements
df.to_csv(outputPath, sep='\t') 



