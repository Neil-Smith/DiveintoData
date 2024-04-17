import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
hour=pd.read_csv('hour.csv')
hour_first48=hour.loc[0:48,:]
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='hr', y='registered', data=hour)
plt.xlabel("Hour")
plt.ylabel("Count")
plt.title("Counts by Hour")
plt.show()

