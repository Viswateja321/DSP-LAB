#implementation of circular convolution using linear convolution result
#by using comment lines instead of its below lines we get different length result of circular convolution
import numpy as np
def linear_convolution(x,h):
	len_x=len(x)
	len_h=len(h)
	conv_len=len_x+len_h-1
	linear_conv=np.zeros(conv_len)
	for i in range(len_x):
		for j in range(len_h):
			linear_conv[i+j]+=x[i] * h[j]
	return linear_conv
def circ_convolution(x,h):
	#N=max(len(x),len(h))
	N=len(x)+len(h)-1
	x=np.pad(x,(0,N-len(x)))
	h=np.pad(h,(0,N-len(h)))
	linear_conv=linear_convolution(x,h)
	circular_conv=np.zeros(N)
	for i in range(N):
		#circular_conv[i] = sum(linear_conv[i + j] for j in range(0, len(linear_conv) - N + 1) if i + j < len(linear_conv))
		circular_conv[i] = linear_conv[i]
	return circular_conv
x=np.array([-5.6,2,7.8,4])
h=np.array([1,3.8,1,-8.9])
print("Linear Convolution Result:", linear_convolution(x,h))
print("Circular convolution result: ",circ_convolution(x,h))
