import pandas as pd 
import numpy as np 
import seaborn as sn 
import random as rn
import matplotlib.pyplot as mat 
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB,MultinomialNB
from sklearn.metrics import accuracy_score

DataFrame1=pd.read_csv('heart.csv') 
DataFrame1

DataFrame2=pd.read_csv('AirQuality.csv',sep=';') 
DataFrame2

DataFrame1.isna().sum().sum()

DataFrame1.dtypes

DataFrame2.dtypes

DataFrame3=DataFrame2.iloc[:,:15]
DataFrame3

DataFrame3.isna().sum().sum()

DataFrame4=DataFrame3.dropna()
DataFrame4

DataFrame4['Date']=pd.to_datetime(DataFrame4['Date'])
DataFrame4

DataFrame4.replace(to_replace=',',value='.',regex=True,inplace=True)
DataFrame4

DataFrame4.drop_duplicates(inplace=True)
DataFrame4

DataFrame1

DataFrame4

DataSet1=DataFrame4[['Date','Time','T','RH','AH']].loc[0:50]
DataSet1.head()

DataSet2=DataFrame4[['Date','Time','T','RH','AH']].loc[51:100]
DataSet2.head()

DataSet3=DataFrame1[['age','sex','cp','ca','target']].loc[50:100]
DataSet3.head()

Merged=pd.concat([DataSet1,DataSet2])
Merged

DataFrame1.loc[DataFrame1['sex']==1,'sex']='M' 

DataFrame1.loc[DataFrame1['sex']==0,'sex']='F'

DataFrame1.head()

from sklearn.preprocessing import LabelEncoder
labelencoder=LabelEncoder()
DataFrame1["sex"]=labelencoder.fit_transform(DataFrame1["sex"])
DataFrame1 

DataFrame1[DataFrame1['ca']==4]

DataFrame1.loc[DataFrame1['ca']==4,'ca']=np.NaN

DataFrame1 = DataFrame1.fillna(DataFrame1.median())

DataFrame1.isnull().sum()

X_train, X_test, y_train, y_test = train_test_split(DataFrame1.iloc[:,:-1], DataFrame1.iloc[:,-1], test_size = 0.3, random_state = 0)

X_train.shape, X_test.shape,y_train.shape

gnb = GaussianNB()

gnb.fit(X_train, y_train)

y_pred = gnb.predict(X_test)
y_pred

print('Model accuracy score: {0:0.4f}'. format(accuracy_score(y_test, y_pred)))