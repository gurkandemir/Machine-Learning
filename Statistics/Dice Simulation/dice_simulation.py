import random
import matplotlib.pyplot as plt
import numpy as np


simulation_cnt = 600000

stats_array = np.zeros(6)

cnt = 0
while cnt < simulation_cnt:
    selected = random.randint(1,6)
    stats_array[selected-1] += 1
    cnt += 1

print stats_array

fig, ax = plt.subplots()
index = np.arange(1,7)
ax.bar(index, stats_array)

plt.show()


### Central Limit Theorem ###
sample_size = 600
sample = np.zeros(6)
samples = []
sample_cnt = 0
cnt = 0
while cnt < simulation_cnt:
    selected = random.randint(1,6)
    sample[selected-1] += 1
    cnt += 1
    sample_cnt += 1
    if sample_cnt == sample_size:
        samples.append(sample)
        sample =  np.zeros(6)
        sample_cnt = 0

sample_means = []
for sample in samples:
    sample_means.append(sample[0]/float(sample_size))

plt.hist(sample_means, bins=20, alpha=0.6)
plt.show()

