import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares,green triangles and solid blue line
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^',[1,20,30,65], 'b-')
plt.show()
plt.close()