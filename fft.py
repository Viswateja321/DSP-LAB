#to implement fft on given input signal 
import numpy as np
x={}
N=len(x)
def fft(x):
	N=len(x)
	if N==1:
		return x
	else:
		xe=x[0::2]
		xo=x[1::2]
		Xe=fft(xe)
		Xo=fft(xo)
		WN=np.exp(-j*2*np.pi*range(0,N/2)/N)
		X=np.concencate[Xe+(WN*Xo),Xe-(WN*Xo)]
		return X
m=fft(x)
print("The fft result of x is: ", m)
