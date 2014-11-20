# -*- coding: utf-8 -*-
print "Hello world"

from numpy import *
from matplotlib import pylab as plt

#xvar = array([1,2,3,4,5])
#yvar = xvar*2
#yvar2 = xvar*1.5

xvar,yvar = loadtxt("../data/data2.csv",unpack=True,delimiter=',')

plt.clf()
plt.plot(xvar,yvar,'rx')
#plt.plot(xvar,yvar2,'b*')
plt.xlim((0,6))
plt.ylim((0,12))
plt.xlabel("variable X")
plt.ylabel("variable Y")
plt.title("Python Plot")
plt.show()
plt.savefig("../fig/fig_python_plot.png")