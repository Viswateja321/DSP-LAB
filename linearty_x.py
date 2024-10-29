import numpy as np
import matplotlib.pyplot as plt
def dtft(x):
	N=len(x)
	n=np.arange(N)
	k=n.reshape((N,1))
	e=np.exp(-2j*np.pi*k*n/N)
	X=np.dot(e,x)
	return X
x1=np.array([1,2,3,4])
x2=np.array([4,8,9,1])
x3=x1+x2
X1=dtft(x1)
X2=dtft(x2)
X3=dtft(x3)
print(X1)
print(X2)
print(X3)
if np.allclose(X3,X1+X2):
	print("Linearity property is verified")
else:
	print("Linearity is not verified")

plt.show()
