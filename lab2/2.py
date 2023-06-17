# a. x[n]  = {1,0,-1,1,2,1}
#    h[n]  = {1,1,1,1}


import numpy as np
import matplotlib.pyplot as plt



x = np.array([1,0,-1,1,2,1])
n1  = np.arange(-2,3+1,1)

h = np.ones(5)
n2 = np.arange(-2,2+1,1)

y = np.convolve(x,h)
n3 = np.arange(-4,5+1,1)


plt.subplot(3,1,1)

plt.xlabel('time_domain')
plt.ylabel('amplitude')
plt.title("Input sequence x[n] ")
plt.grid()
plt.stem(n1,x)

plt.subplot(3,1,2)
plt.grid()
plt.xlabel('time_domain')
plt.ylabel('amplitude')
plt.title("Response sequence h[n] ")
# plt.stem(h)
plt.stem(n2,h)


plt.subplot(3,1,3)

plt.xlabel('time_domain')
plt.ylabel('amplitude')
plt.title("convolution sum y[n] ")
plt.grid()
plt.stem(n3,y)



plt.tight_layout()

plt.show()




print(y)