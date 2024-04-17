import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
hour=pd.read_csv('hour.csv')
hour_first48=hour.loc[0:48,:]
thevariables=['hr','temp','windspeed']
hour_first100=hour.loc[0:100,thevariables]
sns.pairplot(hour_first100, corner=True)
plt.show()

