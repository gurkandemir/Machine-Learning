import numpy as np
import matplotlib.pyplot as plt

lambda_ = 50
data_size = 100
s = np.random.poisson(lambda_, data_size)

count, bins, ignored = plt.hist(s, bins=10, density=True)
plt.show()
