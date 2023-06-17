import numpy as np
import matplotlib.pyplot as plt

t = np.arange(-6, 6, 0.01)
y = (t >= 0).astype(int)



plt.suptitle('Unit step and ramp signals', fontsize=16)

plt.subplot(1, 2, 1)
plt.plot(t, y)

plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Continous time unit step signal')
plt.grid(True)
plt.xlim(-6,6)


t = np.arange(-6, 6, 1)
y = (t >= 0).astype(int)

plt.subplot(1, 2, 2)
plt.stem(t, y)

plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Discrete time unit step signal')
plt.grid(True)


plt.tight_layout()
plt.show()