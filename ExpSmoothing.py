# -*- coding: utf-8 -*-
"""
Module with function to calculate exponential smoothing forecast value
"""


def exponential_forecast(time_series,forecast_value, alpha_value):
    forecast=((alpha_value*time_series[-1]) + ((1-alpha_value)*forecast_value))
    return forecast


def CalculateExpSmoothing(stockPrices, forecast_series, period_series, userInput_alpha):
    i=0
    #open the CSV file
    import csv
    with open('AAPL.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        #loop over all the rows in the csv file
        for row in reader:
            #add stock prices to the list
            stockPrices.insert(i,float(row['Close']))
            #first forecast value is equal to first stock price value
            if i==0:
                smoothing_number=stockPrices[i]
                forecast_series.append(smoothing_number)
            else: 
                #subsequent elements use the formula
                smoothing_number=exponential_forecast(stockPrices,forecast_series[-1],userInput_alpha)
            
            forecast_series.append(smoothing_number)
            period_series.append(i)
            i=i+1 
            