import pandas as pd
import numpy as np 

df=pd.read_csv('"C:/Users/sahil/Desktop/dataset_Facebook.csv"',sep=';') #Read a comma-separated values (csv) file into DataFrame
df

df.describe()

df.shape 

df1=df[['Page total likes','Category','Post Month','Post Weekday']].loc[0:15]
df1

df2=df[['Page total likes','Category','Post Month','Post Weekday']].loc[16:30]
df2

df3=df[['Page total likes','Category','Post Month','Post Weekday']].loc[31:50]
df3

merging=pd.concat([df1,df2,df3])
merging

sorted=df.sort_values('Page total likes',ascending=False)
sorted

trans=df.transpose() 
trans

shaping=df.shape
shaping

pivot_table=pd.pivot_table(df,index=['Type','Paid'],values='like') 
pivot_table