import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

t_narrow = np.linspace(-5, 5, 1000)
impulse_narrow = signal.unit_impulse(1000, 'mid')


t_wide = np.linspace(-5, 5, 100)
impulse_wide = signal.unit_impulse(100, 'mid')



plt.suptitle('Unit Impulse Signal', fontsize=16)

plt.subplot(2, 1, 1)
plt.plot(t_narrow, impulse_narrow)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Unit Impulse Signal (Narrow)')
plt.grid(True)
plt.xlim(-4, 4)


plt.subplot(2, 1, 2)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Unit Impulse Signal (Wide) ')
plt.grid(True)
plt.xlim(-4, 4)
plt.axvline(x=0, color='k')
plt.plot(t_wide, impulse_wide)


plt.tight_layout()
plt.show()
