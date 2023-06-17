import numpy as np
import matplotlib.pyplot as plt

 
n= np.arange(0,10,1)
x= (2**n )* (n>=0)


h = np.ones(5)

y = np.convolve(x,h)

plt.subplot(3,1,1)

plt.xlabel('time_domain')
plt.ylabel('amplitude')

plt.grid()
plt.stem(x)

plt.subplot(3,1,2)
plt.grid()
plt.xlabel('time_domain')
plt.ylabel('amplitude')

plt.stem(h)


plt.subplot(3,1,3)

plt.xlabel('time_domain')
plt.ylabel('amplitude')

plt.grid()
plt.stem(y)


plt.show()