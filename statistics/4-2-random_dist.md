[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> 
import thinkstats2  
import thinkplot  
import numpy as np  
import matplotlib.pyplot as plt  
import random  

nums_to_test = []  
for i in range(100):  
    nums_to_test.append(random.random())  
    
pmf = thinkstats2.Pmf(nums_to_test)  
cdf = thinkstats2.Cdf(nums_to_test)  

thinkplot.Pmf(pmf)  
thinkplot.Config(xlabel='num', ylabel='prob')  
plt.show()  


thinkplot.Cdf(pmf)  
thinkplot.Config(xlabel='num', ylabel='prob')  
plt.show()  

sample = np.random.choice(nums_to_test, 100, replace=True)  
ranks = [cdf.PercentileRank(x) for x in sample]  

rank_cdf = thinkstats2.Cdf(ranks)  
thinkplot.Cdf(rank_cdf)  
plt.show()  

# yes it appears that the distribution is uniform  
