import numpy as np
from matplotlib import pyplot as plt

def u_inf(x):
   return np.exp(-1*np.square(np.tan(x*np.pi-np.pi/2)))

def c(n,x):
   c = u_inf(x)*np.sin(n*np.pi*x)
   return c.sum()/c.size

n_pts=1000001
n_coeffs=500
x = np.linspace(0,1,n_pts)
y = [c(n,x) for n in range(1,n_coeffs,2)]
plt.yscale("log")
plt.plot(range(1,n_coeffs,2),y,"*")
plt.show()
