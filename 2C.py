import pandas as pd
import swifter

df = pd.read_csv('forestfires.csv')

def map_function(row):
    result = row['X'] * row['wind']
    return result

df['map_result'] = df.swifter.apply(map_function, axis=1)
df

reduce_result = df['map_result'].sum()
reduce_result

descriptive_stats=df.describe()
descriptive_stats

grouped_stats=df.groupby('month').agg({'area':['sum','mean','max']})
grouped_stats

import matplotlib.pyplot as plt
df['month'].value_counts().plot(kind='bar')
plt.xlabel('Month')
plt.ylabel('Number of Fires')
plt.title('Number of Fires per Month')
plt.show()

