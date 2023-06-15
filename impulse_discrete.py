import numpy as np
import matplotlib.pyplot as plt


t = np.arange(-6, 6, 1)
y = (t == 0).astype(int)

plt.stem(t, y)

plt.grid(True)
plt.xlabel('n')
plt.ylabel('x[n]')

plt.title('Discrete time unit impulse signal')




plt.show()