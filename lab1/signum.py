import numpy as np
import matplotlib.pyplot as plt


t = np.arange(-6, 6, 0.01)
y = np.sign(t)

plt.suptitle('Signum signals', fontsize=16)

plt.subplot(2, 1, 1)


plt.axvline(x=0, color='k')
plt.axhline(y=0, color='k')
plt.grid(True)

plt.xlabel('n')
plt.ylabel('x[n]')

plt.xlim(-6,6)

plt.title('Continous time')

plt.plot(t, y)


t = np.arange(-6, 6, 1)
y = np.sign(t)

plt.subplot(2, 1, 2)


plt.axvline(x=0, color='k')
plt.grid(True)

plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Discrete time')

plt.stem(t, y)


plt.tight_layout()
plt.show()



