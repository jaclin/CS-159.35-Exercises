from numpy import *
from matplotlib import pylab as plt

fn="../data/data_provinces.csv"

#loading from CSV
#delimiter --> separator
#skiprows --> duh skip rows
#usecols=arange(kung ilang columns)+ilang move to the right
#dtype='a' --> makes it string
name=loadtxt(fn,unpack=True,delimiter=',',skiprows=1,usecols=arange(1),dtype='a')
region=loadtxt(fn,unpack=True,delimiter=',',skiprows=1,usecols=arange(1)+1,dtype='a')
population,lifeExpectancy, \
incomePerCapita,expenditurePerCapita \
= loadtxt(fn,unpack=True,delimiter=",",skiprows=1,usecols=arange(4)+2)

#searches the regions and takes note ilan ung unique
region_list=unique(region)
color_list=array(['red','blue','green','red','blue','green','red','blue','green','red','blue','green','red','blue','green','red','blue'])

#initializes colors to contain ' '
#zeros will make an array full of zeros on how many elements
#dtype='a' --> will make it ' '
colors=zeros(len(name),dtype='a')

#arange(number) --> shows the number of elements
for i in arange(len(name)):
    colors[i]=color_list[region_list==region[i]][0] #gets 0th element ng array
    

plt.clf()
#s = size of circle --> dependent on size of population
#alpha --> transparency
#c --> color
plt.scatter(incomePerCapita,lifeExpectancy,s=population/min(population)*20,alpha=0.5,c=colors)
plt.show()

#show outlier
name[incomePerCapita>12000]

#shows how many regions
len(region_list)

#xvar[1:] kukunin niya til  end
#xvar[:2] from beginning to 2
#min(xvar) = min value
#max(xvar)
#mean(xvar)
#median(xvar)