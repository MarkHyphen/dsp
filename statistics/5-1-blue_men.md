[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>>
import scipy.stats  

mu = 178  
sigma = 7.7  
shortest = 177.8     # in centimeters  
tallest = 185.42   # in centimeters  

dist_norm = scipy.stats.norm(loc=mu, scale=sigma)  
perc_tallest = dist_norm.cdf(tallest)  
perc_shortest = dist_norm.cdf(shortest)  
perc_between_tallest_shortest = perc_tallest-perc_shortest  
print(perc_between_tallest_shortest*100)  
