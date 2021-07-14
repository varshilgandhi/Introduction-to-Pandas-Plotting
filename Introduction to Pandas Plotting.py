# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 19:45:59 2021

@author: abc
"""

#Ploting pandas



import pandas as pd
df = pd.read_csv('manual_vs_auto.csv')

print(df.head())   
#you can title not in our dateset so title unnamed by default

df['Manual'].plot()    #plot the manual dataset
                    
df['Manual'].plot(kind='hist')  #put histogram on dataset

df['Manual'].plot(kind='hist', bins=100)  #declare bins value for that dataset

df['Manual'].plot(kind='hist', bins=100, title='Manual Count') #Give the title of that dataset

df['Manual'].plot(kind='hist', bins=100, title = 'Manual Count', figsize=(12,10)) #fix the size of the plot


##################################################################################################################

#only plot set1 on the dataset 


#change the name of the dataset

import pandas as pd
df = pd.read_csv('Manual_vs_auto.csv')


df = df.rename(columns={'Unnamed: 0':'Image_set'})

print(df.head())


set1_df = df[df['Image_set']=='Set1']
print(set1_df.tail())

#let's input plot 
set1_df['Manual'].plot(kind='hist', bins=30, title = 'Manual Count', figsize=(10,8))



############################################################################################################


import pandas as pd
df = pd.read_csv('manual_vs_auto.csv')

df = df.rename(columns={'Unnamed: 0':'Image_set'})

df['Manual'].plot()    #plot the manual dataset

#rolling avarage on the manual dataset

df['Manual'].rolling(3).mean().plot()


##########################################################################################

#graphical representation of dataset

import pandas as pd
df = pd.read_csv('manual_vs_auto.csv')

df = df.rename(columns={'Unnamed: 0':'Image_set'})

df['Manual'].plot(kind="box", figsize=(8,6))

df.plot(kind='scatter', x='Manual', y='Auto_th_2',title='Manual vs Auto 2')

##########################################################################################

#functions to create category

import pandas as pd
df = pd.read_csv('manual_vs_auto.csv')

df = df.rename(columns={'Unnamed: 0':'Image_set'})

def cell_count(x):
    if x <= 100.0:
        return 'low'
    else:
        return 'high'

#entire manual columns through this function

df['cell_count_index'] = df['Manual'].apply(cell_count)

print(df.head())    
    

df.to_csv('manual_vs_auto.csv') #add this category column in the database

#putting plot into above function category 

df.boxplot(column='Manual', by='cell_count_index')



























