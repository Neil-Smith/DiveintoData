
import pandas as pd

def get_mae(line,actual):
    error=[(x-y) for x,y in zip(line,actual)]
    errorabs=[abs(value) for value in error]
    mae=np.mean(errorabs)
    return(mae)

def get_rmse(line,actual):
    error=[(x-y) for x,y in zip(line,actual)]
    errorsquared=[(value)**2 for value in error]
    rmse=np.sqrt(np.mean(errorsquared))
    return(rmse)

carsales = pd.read_csv('carsales.csv')
carsales.columns = ['month','sales']
carsales = carsales.loc[0:107,:].copy()
carsales['period']=list(range(108))
print(carsales.head())
print(carsales.tail())
from matplotlib import pyplot as plt
#plt.scatter(carsales['period'], carsales['sales'])
#plt.title('Car Sales by Month')
#plt.xlabel('Month')
#plt.ylabel('Sales')
#plt.show()
"""plt.scatter(carsales['period'],carsales['sales'])
plt.plot(carsales['period'],[81.2 * i + 10250.8 for i in \
carsales['period']],'r-',label='Regression Line')
plt.plot(carsales['period'],[125 * i + 8000 for i in
carsales['period']],'r--',label='Hypothesized Line')
plt.legend(loc="upper left")
plt.title('Car Sales by Month')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()"""

saleslist=carsales['sales'].tolist()
regressionline=[81.2 * i + 10250.8 for i in carsales['period']]
hypothesizedline=[125 * i + 8000 for i in carsales['period']]
error1=[(x-y) for x, y in zip(regressionline,saleslist)]
error2=[(x-y) for x, y in zip(hypothesizedline,saleslist)]
import numpy as np
error1abs=[abs(value) for value in error1]
error2abs=[abs(value) for value in error2]
#print(np.mean(error1abs))
#print(np.mean(error2abs))
error1squared=[(value)**2 for value in error1]
error2squared=[(value)**2 for value in error2]
#print(np.sqrt(np.mean(error1squared)))
#print(np.sqrt(np.mean(error2squared)))
#print(get_rmse(regressionline,saleslist))
#print(get_rmse(hypothesizedline,saleslist))

from sklearn.linear_model import LinearRegression

x = carsales['period'].values.reshape(-1,1)
y = carsales['sales'].values.reshape(-1,1)
regressor = LinearRegression()
regressor.fit(x, y)
x_extended = np.append(carsales['period'], np.arange(108, 116))
x_extended=x_extended.reshape(-1,1)
extended_prediction=regressor.predict(x_extended)
"""plt.scatter(carsales['period'],carsales['sales'])
plt.plot(x_extended,extended_prediction,'r--')
plt.title('Car Sales by Month')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()"""

carsales['quadratic']=carsales['period'].apply(lambda x: x**2)
carsales['cubic']=carsales['period'].apply(lambda x: x**3)
x3 = carsales.loc[:,['period','quadratic','cubic']].values.reshape(-1,3)
y = carsales['sales'].values.reshape(-1,1)
regressor_cubic = LinearRegression()
regressor_cubic.fit(x3, y)
"""plt.scatter(carsales['period'],carsales['sales'])
plt.plot(x,regressor.predict(x),'r-')
plt.plot(x,regressor_cubic.predict(x3),'r--')
plt.title('Car Sales by Month')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()
plt.plot(carsales['period'],carsales['sales'])
plt.title('Car Sales by Month')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()"""

import math
carsales['sin_period']=carsales['period'].apply(lambda x: math.sin(x*2*math.pi/12))
carsales['cos_period']=carsales['period'].apply(lambda x: math.cos(x*2*math.pi/12))
x_trig = carsales.loc[:,['period','sin_period','cos_period']].values.reshape(-1,3)
y = carsales['sales'].values.reshape(-1,1)
regressor_trig = LinearRegression()
regressor_trig.fit(x_trig, y)
"""plt.plot(carsales['period'],carsales['sales'])
plt.plot(x,regressor_trig.predict(x_trig),'r--')
plt.title('Car Sales by Month')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()
"""

carsales['squareroot']=carsales['period'].apply(lambda x: x**0.5)
carsales['exponent15']=carsales['period'].apply(lambda x: x**1.5)
carsales['log']=carsales['period'].apply(lambda x: math.log(x+1))
x_complex = carsales.loc[:,['period','log','sin_period','cos_period', \
'squareroot','exponent15','log','quadratic', 'cubic']].values.reshape(-1,9)
y = carsales['sales'].values.reshape(-1,1)
regressor_complex = LinearRegression()
regressor_complex.fit(x_complex,y)

complex_line=[prediction for sublist in regressor_complex.predict(x_complex) \
for prediction in sublist]
print(get_rmse(complex_line,saleslist))
x_complex_train = carsales.loc[0:80,['period', 'log', 'sin_period', 'cos_period', 'squareroot', 'exponent15', 'log','quadratic','cubic']].values.reshape(-1,9)
y_train = carsales.loc[0:80,'sales'].values.reshape(-1,1)
x_complex_test = carsales.loc[81:107,['period','log','sin_period','cos_period','squareroot','exponent15','log','quadratic','cubic']].values.reshape(-1,9)
y_test = carsales.loc[81:107,'sales'].values.reshape(-1,1)
regressor_complex.fit(x_complex_train, y_train)


x_train = carsales.loc[0:80,['period']].values.reshape(-1,1)
x_test = carsales.loc[81:107,['period']].values.reshape(-1,1)
x_trig_train = carsales.loc[0:80,['period','sin_period','cos_period']].values.reshape(-1,3)
x_trig_test = carsales.loc[81:107,['period','sin_period','cos_period']].values.reshape(-1,3)
regressor.fit(x_train, y_train)
regressor_trig.fit(x_trig_train, y_train)
complex_test_predictions=[prediction for sublist in \
regressor_complex.predict(x_complex_test) for prediction in sublist]
test_predictions=[prediction for sublist in regressor.predict(x_test) for \
prediction in sublist]
trig_test_predictions=[prediction for sublist in \
regressor_trig.predict(x_trig_test) for prediction in sublist]
print(get_rmse(test_predictions,saleslist[81:107]))
print(get_rmse(trig_test_predictions,saleslist[81:107]))
print(get_rmse(complex_test_predictions,saleslist[81:107]))
