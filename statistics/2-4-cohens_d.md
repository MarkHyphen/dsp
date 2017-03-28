[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> 
import nsfg
import thinkstats2
import thinkplot
import numpy as np


def CohenEffectSize(group1, group2):
    """Computes Cohen's effect size for two groups.

    group1: Series or DataFrame
    group2: Series or DataFrame

    returns: float if the arguments are Series;
             Series if the arguments are DataFrames
    """
    diff = group1.mean() - group2.mean()

    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / np.sqrt(pooled_var)
    return d

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]

firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

Coh_d_prglngth = CohenEffectSize(firsts.prglngth, others.prglngth)
Coh_d_totalwgt_lb = CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)


# the pregnancy length for first born babies is 0.078 weeks longer than other births on average while first born babies are 0.125 lbs lighter than other births.  The effect of birth order is stronger on birth weight than on length of pregnancy.

