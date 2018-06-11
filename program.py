# -*- coding: utf-8 -*-
"""


"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

from ExpSmoothing import CalculateExpSmoothing,exponential_forecast

 #define list to store values
stockPrices =list()
forecast_series = list()
period_series=list()
smoothing_number=0
invalid_input = True
userInput_alpha = .5


while invalid_input:
    
    #Get user input for Alpha value
    userInput_alpha = input('Enter a value for Alpha between 0 and 1 to use for exponential smoothing ')
    #Ensure Alpha value is a float
    userInput_alpha = float(userInput_alpha)

    CalculateExpSmoothing(stockPrices, forecast_series, period_series, userInput_alpha)
        
    userInput = input('would you like to use this value for Alpha? Y or N ')
    
    #if userInput.upper()=='Y':
    invalid_input = False;
#print values
print('Stock prices', stockPrices)
print(' ')
print('Forecasted values', forecast_series)
print(' ')
print('Predited value = ', forecast_series[-1])
print(' ')

#plot values
plt.plot(stockPrices, label="Values")
plt.plot(forecast_series, label="Forecast")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()


"""
Linear regression calculation
"""
#transform the lists into 2D arrays
x=np.array(period_series)
y=np.array(stockPrices)
x, y = x.reshape(-1,1), y.reshape(-1, 1)
#use linear regression class fit method
model = LinearRegression(fit_intercept=True)
model.fit(x,y)
# Get slope of fitted line
m = model.coef_
# Get y-Intercept of the Line
b = model.intercept_
# Get Predictions for original x values
predictions = model.predict(x)
# Plot the Original Model (Black) and Predictions (Blue)
plt.scatter(x, y,  color='black', label="Values")
plt.plot(x, predictions, color='blue',linewidth=3, label="Linear regression")
plt.scatter(period_series[-1]+1, model.predict(period_series[-1]+1), color='green',linewidth=3, label="Predicted value")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
# following slope intercept form 
print ("Linear regression formula: y = {0}x + {1}".format(m, b) )
print ("Linear regression correlation coeff= ", m)
print('Predited value = ', model.predict(period_series[-1]+1))
