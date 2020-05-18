import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

#Three dices

sample_size = 100
alpha = 0.1

def find_mean(sample):
    return sum(sample) / float(len(sample))


def find_std_dev(sample, mu):
    #mean_of_squares = sum(map(lambda x:x*x, sample))/float(len(sample))
    #variance = mean_of_squares - mu**2
    sum=0
    for i in range(0, len(sample)):
      sum+= (sample[i]-mu)**2

    sum=sum/(len(sample)-1)
    return sum**(1/2.0)

sum_list = []
cnt = 0
while cnt < sample_size:
    selected1 = random.randint(1,6)
    selected2 = random.randint(1,6)
    selected3 = random.randint(1,6)

    sum_ = selected1 + selected2 + selected3
    sum_list.append(sum_)

    cnt += 1

mu = find_mean(sum_list)
std_dev = find_std_dev(sum_list, mu)

degrees_of_freedom = sample_size - 1


actual_mu = 3*(1/6.0*1 + 1/6.0*2 + 1/6.0*3  + 1/6.0*4 + 1/6.0*5 + 1/6.0*6)

print mu
print actual_mu

### Confidence Interval ###
lower_bound = mu - t.ppf(1-alpha/2, degrees_of_freedom) * (std_dev/sample_size**(1/2.0))
upper_bound = mu + t.ppf(1-alpha/2, degrees_of_freedom) * (std_dev/sample_size**(1/2.0))

print lower_bound
print upper_bound


### P Value Experiment ###
t_calc = (mu - actual_mu) / (std_dev/sample_size**(1/2.0))
s = np.random.standard_t(degrees_of_freedom, 100000)
h = plt.hist(s, bins=100, density=True)
plt.show()
if mu < actual_mu:
    print "Calculated probability: " +  str(np.sum(s<t_calc) / float(len(s)))
    print "Actual probabilityt:" + str(t.cdf(t_calc, degrees_of_freedom))
else:
    print np.sum(s>t_calc) / float(len(s))
    print "Actual probability: " + str(1 - t.cdf(t_calc, degrees_of_freedom))
