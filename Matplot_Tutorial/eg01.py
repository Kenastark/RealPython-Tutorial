import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro');  # Plot some data on the axes.
plt.axis([0, 6, 0, 20]) # (xmin, xmax, ymin, ymax)
plt.show()
plt.close()