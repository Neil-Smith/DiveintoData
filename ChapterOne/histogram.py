import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
hour=pd.read_csv('hour.csv')
hour_first48=hour.loc[0:48,:]
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(hour['count'],bins=80)
plt.xlabel("Ridership")
plt.ylabel("Frequency")
plt.title("Ridership Histogram")
plt.show()

