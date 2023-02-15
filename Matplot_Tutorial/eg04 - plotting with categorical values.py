import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3), facecolor='red') # creates a figure. figsize gives the size of the of the plot window in width, height in inches
plt.subplot(131)  # (3,1,1) i.e 3 rows, 1 column, 1st index
plt.bar(names, values)
plt.subplot(132) 
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()
plt.close()
# (3,1,1) i.e 3 rows, 1 column, 1st index
# (132) i.e 1 row, 3 columns, 2nd index