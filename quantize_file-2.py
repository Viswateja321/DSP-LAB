'''
Algorithm:
1. Take an input signal from the user
2. sample it with certain sampling frequency
3. Now quantize the sampled signal by choosing no.of levels we need.
4. the quantized signal will be given as the total input x value/no.of levels .
5. By converting into binary values we can get the digital signal.
'''
import numpy as np
from matplotlib import pyplot as plt
dur=0.5
fs=8000
t=np.arange(0,dur,1.0/fs)
x=np.sin(2*np.pi*200*t)
t2=np.arange(0,int(dur*fs),8)
y=x[t2] #resampled signal
#plt.plot(x)
#plt.plot(y)
#plt.show()
yrange=np.max(y)+abs(np.min(y))
print(np.max(y),np.min(y),yrange)
L=input('enter no of quantization levels')
step=yrange/float(L)
q_levels=np.arange(np.min(y),np.max(y),step)
print(q_levels)
z=[]
for i in y:
    z.append(q_levels[np.argmin(abs(q_levels-i))])
print(z)
plt.plot(z)
plt.show()
    
