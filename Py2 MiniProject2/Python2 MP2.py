#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 13:25:27 2018

@author: byacoube
"""

import matplotlib.pyplot as plt
import numpy as np
from io import StringIO
import csv
import itertools

class IndexCorrelation:
    
    def LoadCSVFile(filename):
         
        stockPrices = list()
        stockPrices.clear()
        try:
            with open(filename, newline='') as csvfile:
                reader1 = csv.DictReader(csvfile)
                
                i=0
                #loop over all the rows in the csv file
                for row in reader1:
                    #add stock prices to the list
                    stockPrices.insert(i,float(row['Close']))
                    i=i+1
                    
        except Exception as ex:
            print(ex)
        
        return stockPrices

def main():
    """
    Main program flow
    """

    try:
    
        
        stockPrices1 = list();
        stockPrices2 = list();
        
        indexSymbol1  = input('Enter a number for the first Stock Index between 1 and 7; 1-DJI, 2-FCHI, 3-GDAXI, 4-GSPC, 5-HSI, 6-IXIC, 7-N225 : ')
        indexSymbol2  = input('Enter a number for the second Stock Index between 1 and 7; 1-DJI, 2-FCHI, 3-GDAXI, 4-GSPC, 5-HSI, 6-IXIC, 7-N225 : ')
        indexSymbol3  = input('Enter a number for the third Stock Index between 1 and 7; 1-DJI, 2-FCHI, 3-GDAXI, 4-GSPC, 5-HSI, 6-IXIC, 7-N225 : ')
        indexSymbol4  = input('Enter a number for the fourth Stock Index between 1 and 7; 1-DJI, 2-FCHI, 3-GDAXI, 4-GSPC, 5-HSI, 6-IXIC, 7-N225:  ')
        indexSymbol5  = input('Enter a number for the fifth Stock Index between 1 and 7; 1-DJI, 2-FCHI, 3-GDAXI, 4-GSPC, 5-HSI, 6-IXIC, 7-N225 : ')
        
        #get all combinations of the 5 selected indices
        for comb in itertools.combinations([indexSymbol1, indexSymbol2, indexSymbol3, indexSymbol4,indexSymbol5], 2):
            stockPrices1 = IndexCorrelation.LoadCSVFile(comb[0]+".csv")
            stockPrices2 = IndexCorrelation.LoadCSVFile(comb[1]+".csv")
            
            #remove all elements in the lists except prices for the last 10 years monthly closes (i.e. last 120 numbers)
            n1 = len(stockPrices1)-120
            n2 = len(stockPrices2)-120
            stockPrices1 = stockPrices1[n1:]
            stockPrices2 = stockPrices2[n2:] 
            
            
            x0 = range(len(stockPrices1))
            # plot the two stock market indices
            plt.plot(x0, stockPrices1, label="Index " + comb[0])      # plot of index1 data
            plt.plot(x0, stockPrices2, label="Index " + comb[1])      # plot of index2 data
            plt.legend()
            plt.show()
            #calculate the correlation matrix
            corrMatrix = np.corrcoef(stockPrices1,stockPrices2)
            print("Correlation matrix =  " )
            print( corrMatrix)
            # plot a scatter plot of the two stock market indices
            plt.scatter( stockPrices1,stockPrices2, label="Correlation between Index " + comb[0] +" and index " + comb[1])      # plot of index1 data
            plt.legend()
            plt.show()
            
            
    except Exception as ex:
        print(ex)
                    

if __name__ == '__main__':
    main()