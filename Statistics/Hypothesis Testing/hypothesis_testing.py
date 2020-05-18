import numpy as np
from scipy.stats import norm

'''
% A neurologist is testing the effect of a drug on response time by
% injecting 100 rats with a unit dose of the drug, subjecting each to
% neurological stimulus and recording its response time. The neurologist
% knows that the mean response time for rats not injected with the drug is
% 1.2 seconds with the sample standard deviation of 0.5 seconds. The mean
% of the 100 injected rats response times is 1.05 seconds . Do you think
% that the drug has an affect on response time? You can make normality
assumption.

% H0: Drug has no effect => sample_mean = actual_mean
% H1: Drug has effect    => sample_mean < actual_mean
'''

actual_mean = 1.2
actual_std_dev = 0.5

sample_size = 1000
sample_mean = 1.05
sample_std_dev = actual_std_dev / sample_size**(1/2.0)

z = (sample_mean - actual_mean) / sample_std_dev

p_value = norm.cdf(z)

alpha = 0.05
print p_value

if p_value < alpha:
    print "NULL HYPOTHESIS REJECTED"
else:
    print "NULL HYPOTHESIS CAN NOT BE REJECTED"
