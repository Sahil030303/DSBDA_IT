import pandas as pd #Python library used for working with data sets
import numpy as np #Python library used for working with arrays
import seaborn as sn # library for making statistical graphics in Python
import matplotlib.pyplot as plt #used to create 2D graphs and plots by using python scripts

df1=pd.read_csv('dataset_Facebook.csv',sep=';') 
df1.head()

# Plotting graphs
plt.figure(figsize=(12, 8))  # Set the figure size
# Bar plot of Total Interactions
plt.subplot(2, 2, 1)  # Create a subplot (2 rows, 2 columns, subplot 1)
plt.bar(df1['Type'], df1['Total Interactions'])
plt.xlabel('Type')
plt.ylabel('Total Interactions')
plt.title('Total Interactions by Type')

# Scatter plot of Lifetime Post Total Reach vs. Lifetime Post Total Impressions
plt.subplot(1, 1, 1)  # Create a subplot (2 rows, 2 columns, subplot 2)
plt.scatter(df1['Lifetime Post Total Reach'], df1['Lifetime Post Total Impressions'], alpha=0.5)
plt.xlabel('Lifetime Post Total Reach')
plt.ylabel('Lifetime Post Total Impressions')
plt.title('Lifetime Post Total Reach vs. Impressions')

# Histogram of Lifetime Engaged Users
plt.subplot(1, 1 ,1 )  # Create a subplot (2 rows, 2 columns, subplot 3)
plt.hist(df1['Lifetime Engaged Users'], bins=20, edgecolor='k')
plt.xlabel('Lifetime Engaged Users')
plt.ylabel('Frequency')
plt.title('Lifetime Engaged Users Distribution')

# Box plot of Lifetime Post Consumers by Category
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

