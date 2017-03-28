[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>>
import nsfg  
import thinkstats2  
import thinkplot  
import numpy as np  
import matplotlib.pyplot as plt  

def BiasPMF(pmf, label):  
    new_pmf = pmf.Copy(label=label)  

    for x, p in pmf.Items():  
        new_pmf.Mult(x, x)  

    new_pmf.Normalize()  
    return new_pmf  


resp = nsfg.ReadFemResp()  
  
# actual dist  
pmf_numkdhh_unbiased = thinkstats2.Pmf(resp.numkdhh, label='unbiased numkdhh')  
thinkplot.Hist(pmf_numkdhh_unbiased)  
thinkplot.Config(xlabel='num children in family', ylabel='unbiased prob')  
plt.show()  

# biased dist  
pmf_numkdhh_biased = BiasPMF(pmf_numkdhh_unbiased, label='biased numkdhh')  
thinkplot.Hist(pmf_numkdhh_unbiased)  
thinkplot.Config(xlabel='num children in family', ylabel='biased prob')  
plt.show()  

print(pmf_numkdhh_unbiased.Mean())  
print(pmf_numkdhh_biased.Mean())  
