import numpy as np
from scipy.stats import norm, t
import matplotlib.pyplot as plt

'''
Textbook Chapter 9.9

A study published in Chemosphere reported the levels of the dioxin TCDD of 20
Massachusetts Vietnam veterans who were possibly exposed to Agent Orange.

Find a 95% confidence interval for mu_1 - mu_2, where mu1 and mu2 represent the
true mean TCDD levels in plasma and in fat tissue, respectively.

Assume the distribution of the differences to be approximately normal.
'''

# TCDD level in plasma 
x1 = np.array([2.5, 3.1, 2.1, 3.5, 3.1, 1.8, 6.0, 3.0, 36.0, 4.7, 6.9, 3.3, 4.6, 1.6,
      7.2, 1.8, 20.0, 2.0, 2.5, 4.1]);

# TCDD levels in fat tissue
x2 = np.array([4.9, 5.9, 4.4, 6.9, 7.0, 4.2, 10.0, 5.5, 41.0, 4.4, 7.0, 2.9, 4.6, 1.4,
      7.7, 1.1, 11.0, 2.5, 2.3, 2.5]);

alpha = 0.05
sample_size1 = len(x1);
sample_size2 = len(x2);

################
### UNPAIRED ###
################
mean_d    = np.mean(x1) - np.mean(x2)
std_dev_d = (np.var(x1) / float(sample_size1) + np.var(x2) /
          float(sample_size2))**(1/2.0)

degrees_of_freedom = (np.var(x1) / float(sample_size1) + np.var(x2) /
          float(sample_size2))**2 / ((np.var(x1)/float(sample_size1))**2/(sample_size1-1) + (np.var(x2)/float(sample_size1))**2/(sample_size1-1))


data = np.random.normal(mean_d, std_dev_d, size=1000)

plt.hist(data, bins=10, density=True, alpha=0.6, color='g')


# Plot the PDF.
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mean_d, std_dev_d)

plt.plot(x, p, 'k', linewidth=2)

plt.show()

#Confidence interval for mu1 - mu2, variences are not equal, both unknown
lower_bound = mean_d - t.ppf(1-alpha/2, degrees_of_freedom) * (std_dev_d/sample_size1**(1/2.0))
upper_bound = mean_d + t.ppf(1-alpha/2, degrees_of_freedom) * (std_dev_d/sample_size1**(1/2.0))

print "Lower Bound: " + str(lower_bound)
print "Upper Bound: " + str(upper_bound)


##############
### PAIRED ###
##############

degrees_of_freedom = sample_size1 - 1

mean_d    = np.mean(np.subtract(x1,x2))
std_dev_d = (np.var(np.subtract(x1,x2)) / float(sample_size1-1))**(1/2.0)

data = np.random.normal(mean_d, std_dev_d, size=1000)

plt.hist(data, bins=10, density=True, alpha=0.6, color='g')

# Plot the PDF.
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mean_d, std_dev_d)

plt.plot(x, p, 'k', linewidth=2)

plt.show()

#Confidence interval for paired observations
lower_bound = mean_d - t.ppf(1-alpha/2, degrees_of_freedom) * (std_dev_d/sample_size1**(1/2.0))
upper_bound = mean_d + t.ppf(1-alpha/2, degrees_of_freedom) * (std_dev_d/sample_size1**(1/2.0))

print "Lower Bound: " + str(lower_bound)
print "Upper Bound: " + str(upper_bound)
