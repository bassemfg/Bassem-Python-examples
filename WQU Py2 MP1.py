
import csv
import quandl
import matplotlib.pyplot as plt
import numpy as np
import numpy as np_data
from io import StringIO
from scipy.interpolate import interp1d
from scipy.optimize import leastsq
import numpy.polynomial.polynomial as poly

quandl.ApiConfig.api_key ='RqpDsLqAEJyHa7iAADNQ'



try:    
    stockSymbol = input('Enter a quandl stock symbol: ')
    data = quandl.Dataset('WIKI/'+stockSymbol).data(params={ 'start_date':'2018-01-01', 'end_date':'2018-01-31'})   
    data_array= []
    csv_data = data.to_csv()
    
except Exception as e:
   print('please enter a valid symbol' + e)
   exit
   

try:    
    i=0
    reader = csv.reader(csv_data.split('\n'), delimiter=',')    
    for row in reader:
        #skip the row header as it is string not float
        if i>0 and row[4] :
            data_array.append(float(row[4]))
        i=i+1
except Exception as ex:
    error=ex            
finally: 
    print(data_array)

# Original "data set" --- 21 samples for January daily closing prices.
x0 = range(len(data_array))     # 0 to data length, step 1
y0 = data_array                 # downloaded close price values

# original plot
plt.plot(x0, y0, 'o', label='Data')

# Array with points in between those of the data set for interpolation.
x = np.linspace(0, len(data_array)-1)

f = interp1d(x0, y0, kind='quadratic')    # interpolation function
plt.plot(x, f(x), label='quadratic')      # plot of interpolated data

plt.legend()
plt.show()

#############################################################################

x_sqrd = [i**2 for i in x0]
# here, create lambda functions for Line, Quadratic fit
# tpl is a tuple that contains the parameters of the fit
funcLine=lambda tpl,x0 : tpl[0]*x0+tpl[1]
# func is going to be a placeholder for funcLine,funcQuad or whatever 
# function we would like to fit
func=funcLine
# ErrorFunc is the diference between the func and the y "experimental" data
ErrorFunc=lambda tpl,x0,y0: func(tpl,x0)-y0
#tplInitial contains the "first guess" of the parameters 
tplInitial1=(1.0,2.0)
# leastsq finds the set of parameters in the tuple tpl that minimizes
# ErrorFunc=yfit-yExperimental
tplFinal1,success=leastsq(ErrorFunc,tplInitial1[:],args=(x0,y0))
print (" linear fit ",tplFinal1)
xx1=np.linspace(0, len(data_array)-1,len(data_array))
yy1=func(tplFinal1,xx1)
#------------------------------------------------
# now the quadratic fit
#-------------------------------------------------
funcQuad=lambda tpl,x0 : np.float64(tpl[0])*np.float64(x_sqrd)+np.float64(tpl[1])*np.float64(x0)+np.float64(tpl[2])
func=funcQuad
tplInitial2=(1.0,2.0,3.0)

tplFinal2,success=leastsq(ErrorFunc,tplInitial2[:],args=(x0,y0))
print ("quadratic fit" ,tplFinal2)
xx2=np.array(xx1)

yy2=func(tplFinal2,xx2)
plt.plot(xx1,yy1,'r-',label='leastsq linear')
plt.plot(x0,y0,'bo')
plt.plot(xx2,yy2,'g-',label='leastsq quadratic')
plt.legend()
plt.show()

#using polyfit
coefs = poly.polyfit(x0, y0, 2)
ffit = poly.polyval(xx2, coefs)
plt.plot(x0,y0,'bo')
plt.plot(xx2, ffit,'g', label='Polyfit quadratic')
plt.legend()
plt.show()
