import numpy as np
import matplotlib.pyplot as pt
x1=[1,2,3]
x2=[1,1,1]
x3=np.convolve(x1,x2)
n=len(x1)
def dtft(x,n):
    w=np.arange(-np.pi,np.pi,0.01)
    X=np.zeros(len(w),dtype=complex)
    for k in range(len(w)):
        X[k]=sum(x[i]*np.exp(-1j*w[k]*i) for i in range(n))
    return w,X
w,X_3=dtft(x3,len(x3))
pt.figure(figsize=(8,4))
pt.title("X_3(W)")
pt.plot(w,np.abs(X_3))
w,X1=dtft(x1,n)
w,X2=dtft(x2,n)
X3=X1*X2
pt.figure(figsize=(8,4))
pt.title("X3(W)")
pt.plot(w,np.abs(X3),color='gold')
if(X3.all()==X_3.all()):
    print("convolution theorem verified")