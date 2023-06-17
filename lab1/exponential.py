import numpy as np
import matplotlib.pyplot as plt


a=-1
t = np.arange(-6, 6, 0.01)
y = np.exp(t*a)

plt.suptitle('Exponential signals', fontsize=16)

plt.subplot(2, 2, 1)


plt.axvline(x=0, color='k')
plt.axhline(y=0, color='k')
plt.grid(True)

plt.xlabel('n')
plt.ylabel('x[n]')

plt.title('Continous time for a = -1')


plt.plot(t, y)


a=1
t = np.arange(-6, 6, 0.01)
y = np.exp(t*a)

plt.subplot(2, 2, 2)


plt.axvline(x=0, color='k')
plt.axhline(y=0, color='k')
plt.grid(True)

plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Continous time for a = 1')

plt.plot(t, y)



a=-1
t = np.arange(-6, 6, 1)
y = np.exp(t*a)

plt.subplot(2, 2, 3)


plt.axvline(x=0, color='k')
plt.axhline(y=0, color='k')
plt.grid(True)

plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Discrete time for a = -1')

plt.stem(t, y)



a=1
t = np.arange(-6, 6, 1)
y = np.exp(t*a)

plt.subplot(2, 2, 4)


plt.axvline(x=0, color='k')
plt.axhline(y=0, color='k')
plt.grid(True)

plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Discrete time for a = 1')

plt.stem(t, y)



plt.tight_layout()
plt.show()