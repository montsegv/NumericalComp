#
# select a distribution from random
# produce random numbers on such a distribution
# 
# zeeAlso
# en.wikipedia.org/wiki/Probability_distribution
#

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
a = np.random.binomial(n = 5, p = 0.7, size = 20)
print(a)
sns.distplot(a, hist=True, kde=False)
plt.ylabel('Muestras')
plt.xlabel('Intervalos')
plt.show()