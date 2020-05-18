import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

target_mu = 10
target_std_dev = 2
data_size = 500

print "Target mean: " + str(target_mu)
print "Target standard deviation: " + str(target_std_dev)

# Generate some data for this demonstration.
data = np.random.normal(target_mu, target_std_dev, size=data_size)
#print data

# Fit a normal distribution to the data:
sum_data = 0
for d in data:
    sum_data += d

data_mu  = sum_data / data_size
print "Data mean: " + str(data_mu)

squared_sum_data = 0
for d in data:
  squared_sum_data+= (d-data_mu)**2

data_var = squared_sum_data / (data_size-1)
data_std_dev = data_var**(1/2.0)
print "Data varience: " + str(data_var)
print "Data standard deviation: " + str(data_std_dev)

plt.hist(data, bins=15, density=True, alpha=0.8, color='g')

# Plot the PDF.
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, data_mu, data_std_dev)
t = norm.pdf(x, target_mu, target_std_dev)
plt.plot(x, t, 'r--')
plt.plot(x, p, 'k', linewidth=2)
title = "Fit results: mu = %.2f,  std = %.2f" % (data_mu, data_std_dev)
plt.title(title)

plt.show()
