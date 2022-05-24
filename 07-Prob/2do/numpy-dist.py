#
# select a distribution from numpy
# produce random numbers on such a distribution
# 
# zeeAlso
# en.wikipedia.org/wiki/Probability_distribution
#

# import numpy
import numpy as np
import matplotlib.pyplot as plt
  
# Using triangular() method
gfg = np.random.triangular(-5, 0, 5, 5000)
  
plt.hist(gfg, bins = 50, density = True)
plt.show()