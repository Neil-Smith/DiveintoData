
import pandas as pd
carsales = pd.read_csv('carsales.csv')
carsales.columns = ['month','sales']
carsales = carsales.loc[0:107,:].copy()
carsales['period']=list(range(108))
x = carsales['period'].values.reshape(-1,1)
y = carsales['sales'].values.reshape(-1,1)
#print(x)
#print(y)
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x, y)
print(regressor.coef_)
print(regressor.intercept_)
