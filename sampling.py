#generated a cos wave and sampling it
import numpy as np ,scipy
from matplotlib import pyplot as plt
t_min=-1
t_max=1
num_t=1000
t=np.linspace(t_min,t_max,num_t)
f=3
xt=np.cos(2*np.pi*f*t)
plt.plot(t,xt)
plt.xlabel("t")
plt.ylabel("Amplitude")
plt.title("plot of cos(2*np.pi*f*t)")
plt.show()
Fs=5#sampling frequency
ts=1/Fs
pulse_train=np.arange(t_min,t_max,ts)#creating pulse train for sampling
plt.stem(pulse_train,np.ones(len(pulse_train)))
plt.show()
xt_sampled=np.cos(2*np.pi*f*pulse_train)
plt.stem(pulse_train,xt_sampled)
plt.plot(t,xt,'r')
plt.show()
x_rs,t_rs=scipy.signal.resample(xt_sampled,1000,pulse_train)
plt.plot(t_rs,x_rs,'b')
plt.plot(t,xt,'o')
plt.show()
