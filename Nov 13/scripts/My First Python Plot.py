from numpy import *
from matplotlib import pylab as plt

xvar = array([1,2,3,4,5])
yvar = xvar*2

plt.clf()
plt.plot(xvar,yvar,'rx')

plt.xlim((0,6))
plt.ylim((0,12))

plt.xlabel("variable X")
plt.ylabel("variable Y")

plt.title("My First Python Plot")
plt.savefig("../fig/fig_first_plot.png")