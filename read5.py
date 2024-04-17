
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
hour = pd.read_csv('hour.csv')
print(hour.head())
print(hour['count'].median())
print(hour['count'].std())
print(hour['registered'].min())
print(hour['registered'].max())
print(hour.describe())
print(hour.loc[3,'count'])
print(hour.loc[2:4,'registered'])
print(hour.loc[(hour['hr']<5) & (hour['temp']<.50),'count'].mean())
print(hour.loc[(hour['hr']<5) & (hour['temp']>.50),'count'].mean())
print(hour.loc[(hour['temp']>0.5) | (hour['hum']>0.5),'count'].mean())
print(hour.groupby(['season'])['count'].mean())
print(hour.groupby(['season','holiday'])['count'].mean())
print(hour['casual'].corr(hour['registered']))
print(hour['temp'].corr(hour['hum']))
thenames=['hr','temp','windspeed']
cor_matrix = hour[thenames].corr()
print(cor_matrix)
plt.figure(figsize=(14,10))
corr = hour[thenames].corr()
sns.heatmap(corr, annot=True,cmap='binary',
fmt=".3f",
xticklabels=thenames,
yticklabels=thenames)
plt.show()
# Create a pivot table
df_hm =hour.pivot_table(index = 'hr',columns ='weekday',values ='count')
# Draw a heatmap
plt.figure(figsize = (20,10)) # To resize the plot
sns.heatmap(df_hm, fmt="d", cmap='binary',linewidths=.5, vmin = 0)
plt.show()
