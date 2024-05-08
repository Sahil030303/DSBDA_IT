import pandas as pd #Python library used for working with data sets
import numpy as np #Python library used for working with arrays
import seaborn as sn # library for making statistical graphics in Python
import matplotlib.pyplot as mat #used to create 2D graphs and plots by using python scripts

df2=pd.read_csv('heart.csv')

import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
plt.subplot(2, 2, 1)  # Create a subplot (2 rows, 2 columns, subplot 1)
plt.hist(df2['age'], bins=10, edgecolor='k')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')
plt.show()

plt.subplot(2, 2, 2)  # Create a subplot (2 rows, 2 columns, subplot 2)
sex_counts = df2['sex'].value_counts()
plt.bar(sex_counts.index, sex_counts.values)
plt.xlabel('Sex (0 = female, 1 = male)')
plt.ylabel('Count')
plt.title('Gender Distribution')

plt.subplot(2, 2, 3)  # Create a subplot (2 rows, 2 columns, subplot 3)
plt.scatter(df2['age'], df2['chol'], alpha=0.5)
plt.xlabel('Age')
plt.ylabel('Cholesterol')
plt.title('Age vs. Cholesterol')

plt.subplot(2, 2, 4)  # Create a subplot (2 rows, 2 columns, subplot 4)
plt.boxplot([df2[df2['target'] == 0]['trestbps'],
             df2[df2['target'] == 1]['trestbps']],
            labels=['No Disease', 'Disease'])
plt.xlabel('Target')
plt.ylabel('Resting Blood Pressure')
plt.title('Resting Blood Pressure by Target')
plt.tight_layout()  
plt.show()

df3=pd.read_csv('AirQuality.csv', sep=';')
df3.head()

plt.subplot(2, 2, 2)  # Create a subplot (2 rows, 2 columns, subplot 2)
plt.scatter(df3['NOx(GT)'], df3['NO2(GT)'], alpha=0.5)
plt.xlabel('NOx(GT)')
plt.ylabel('NO2(GT)')
plt.title('NOx(GT) vs. NO2(GT)')

plt.subplot(2, 2, 4)  # Create a subplot (2 rows, 2 columns, subplot 4)
plt.scatter(df3['NO2(GT)'], df3['PT08.S4(NO2)'], alpha=0.5)
plt.xlabel('NO2(GT)')
plt.ylabel('PT08.S4(NO2)')
plt.title('NO2(GT) vs. PT08.S4(NO2)')
plt.tight_layout()  # Adjust the spacing between subplots
plt.show()

# Scatter plot of PT08.S1(CO) vs. PT08.S2(NMHC)
plt.subplot(2, 2, 2)  # Create a subplot (2 rows, 2 columns, subplot 2)
plt.scatter(df3['PT08.S1(CO)'], df3['PT08.S2(NMHC)'], alpha=0.5)
plt.xlabel('PT08.S1(CO)')
plt.ylabel('PT08.S2(NMHC)')
plt.title('PT08.S1(CO) vs. PT08.S2(NMHC)')

df1=pd.read_csv('dataset_Facebook.csv',sep=';') 
df1.head()

plt.figure(figsize=(12, 8))  # Set the figure size
plt.subplot(2, 2, 1)  # Create a subplot (2 rows, 2 columns, subplot 1)
plt.bar(df1['Type'], df1['Total Interactions'])
plt.xlabel('Type')
plt.ylabel('Total Interactions')
plt.title('Total Interactions by Type')

plt.subplot(1, 1, 1)  # Create a subplot (2 rows, 2 columns, subplot 2)
plt.scatter(df1['Lifetime Post Total Reach'], df1['Lifetime Post Total Impressions'], alpha=0.5)
plt.xlabel('Lifetime Post Total Reach')
plt.ylabel('Lifetime Post Total Impressions')
plt.title('Lifetime Post Total Reach vs. Impressions')

plt.subplot(1, 1 ,1 )  # Create a subplot (2 rows, 2 columns, subplot 3)
plt.hist(df1['Lifetime Engaged Users'], bins=20, edgecolor='k')
plt.xlabel('Lifetime Engaged Users')
plt.ylabel('Frequency')
plt.title('Lifetime Engaged Users Distribution')

plt.subplot(1, 1, 1)  # Create a subplot (2 rows, 2 columns, subplot 4)
plt.boxplot([df1[df1['Category'] == 1]['Lifetime Post Consumers'],
             df1[df1['Category'] == 2]['Lifetime Post Consumers'],
             df1[df1['Category'] == 3]['Lifetime Post Consumers']],
            labels=['Category 1', 'Category 2', 'Category 3'])
plt.xlabel('Category')
plt.ylabel('Lifetime Post Consumers')
plt.title('Lifetime Post Consumers by Category')
plt.tight_layout()  # Adjust the spacing between subplots
plt.show()  # Display the plots

