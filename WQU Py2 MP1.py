
import quandl
import matplotlib.pyplot as plt
import numpy as np
import numpy as np_data
from io import StringIO
import csv
from scipy.interpolate import interp1d

quandl.ApiConfig.api_key ='RqpDsLqAEJyHa7iAADNQ'

stockSymbol = input('Enter a quandl stock symbol: ')


#try:
data = quandl.Dataset('WIKI/'+stockSymbol).data(params={ 'start_date':'2018-01-01', 'end_date':'2018-01-31'})
i=0
data_array= []
csv_data = data.to_csv()

reader = csv.reader(csv_data.split('\n'), delimiter=',')
try:
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

#except Exception as e:
#   print( e)
    
   # data provided
   x=np.array([1.0,2.5,3.5,4.0,1.1,1.8,2.2,3.7])
   y=np.array([6.008,15.722,27.130,33.772,5.257,9.549,11.098,28.828])
   # here, create lambda functions for Line, Quadratic fit
   # tpl is a tuple that contains the parameters of the fit
   funcLine=lambda tpl,x : tpl[0]*x+tpl[1]
   funcQuad=lambda tpl,x : tpl[0]*x**2+tpl[1]*x+tpl[2]
   # func is going to be a placeholder for funcLine,funcQuad or whatever 
   # function we would like to fit
   func=funcLine
   # ErrorFunc is the diference between the func and the y "experimental" data
   ErrorFunc=lambda tpl,x,y: func(tpl,x)-y
   #tplInitial contains the "first guess" of the parameters 
   tplInitial1=(1.0,2.0)
   # leastsq finds the set of parameters in the tuple tpl that minimizes
   # ErrorFunc=yfit-yExperimental
   tplFinal1,success=leastsq(ErrorFunc,tplInitial1[:],args=(x,y))
   print " linear fit ",tplFinal1
   xx1=np.linspace(x.min(),x.max(),50)
   yy1=func(tplFinal1,xx1)
   #------------------------------------------------
   # now the quadratic fit
   #-------------------------------------------------
   func=funcQuad
   tplInitial2=(1.0,2.0,3.0)

   tplFinal2,success=leastsq(ErrorFunc,tplInitial2[:],args=(x,y))
   print "quadratic fit" ,tplFinal2
   xx2=xx1

   yy2=func(tplFinal2,xx2)
   plt.plot(xx1,yy1,'r-',x,y,'bo',xx2,yy2,'g-')
   plt.show()
   
from numpy import random , histogram , arange , sqrt , exp , nonzero, array
from scipy.optimize import leastsq
import pylab
if __name__ == '__main__':
n = 1000; isi=random.exponential(0.1 , size=n)
db = 0.01; bins = arange (0 ,1.0 , db)
h = histogram(isi,bins)[0]
p = h.astype(float)/n/db
# Function to be fit
# x: independent variable
# p: tuple of parameters
fitfunc = lambda p,x:exp(-x/p[0])/p[0]
# Standard form, here err is absolute error
errfunc= lambda p, x , y , err : (y - fitfunc (p, x))/err
# Initial values for fit parameters
initialFitP = array([0.2])
# Hist count less than four has poor estimate of the weight
# Don't use in the fitting process
idx = nonzero(h>4)
out = leastsq( errfunc, initialFitP, args=( bins[idx] +0.01/2 , p[idx] ,p[idx] /sqrt(h[idx])))
l1 = 'Actual Data Points'
pylab.errorbar( bins[idx],p[idx], yerr=p[idx]/sqrt(h[idx]), fmt='ko', label=l1, color='red' )
l2 = 'Best Fit'
pylab.plot(bins,fitfunc((out[0],),bins),'b--',lw=2,label=l2 )
pylab.legend()
pylab.show ()