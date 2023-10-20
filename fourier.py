import numpy as np
from matplotlib import pyplot as plt

def c(n,x):
   c = np.sin(2*np.pi*x)*np.sin(n*np.pi*x)
   return c.sum()/c.size

n_pts=101
x = np.linspace(0,1,n_pts)
print(x)
y = [c(n,x) for n in range(1,10)]

plt.plot(range(1,10),y)
# plt.plot(y2)
plt.show()
