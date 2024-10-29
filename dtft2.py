import numpy as np
from matplotlib import pyplot as plt
#import cmath
def dtft(x):
	X=[]
	w=np.arange(-np.pi,np.pi,0.0001*np.pi)
	for f in w:
		s=0
		for n in range(0,len(x)): 
			s=s+x[n]*np.exp(-1j*f*n)
		X.append(s)
	return w,X
n=np.arange(0,500)
h=np.sin(2*np.pi*200/8000*n)
w,X=dtft(h)
x_mag=np.abs(X)
x_ang=np.angle(X)
plt.subplot(2,1,1)
plt.plot(w,x_mag)
plt.subplot(2,1,2)
plt.plot(w,x_ang)

plt.show()
