import numpy as np
from matplotlib import pyplot as pt
x1=[1,2,3,4,5]
x2=[1,1,1,1,1]
n=len(x1)
x3=np.zeros(n)
for i in range(n):
    x3[i]=x1[i]+x2[i]
def dtft(x, n):
    w=np.arange(-np.pi,np.pi,0.01)
    X=np.zeros(len(w),dtype=complex)
    for k in range(len(w)):
        X[k]=sum(x[i]*np.exp(-1j*w[k]*i) for i in range(n))
    return w,X
w,X3=dtft(x3,n)
w,Y1=dtft(x1,n)
w,Y2=dtft(x2,n)
z=len(Y1)
Y3=np.zeros(z,dtype=complex)
for i in range(z):
    Y3[i]=Y1[i]+Y2[i]
pt.figure(figsize=(8,4))
pt.title('x1+x2=x3')
pt.plot(w,np.abs(X3))
pt.figure(figsize=(8,4))
pt.title('y1+y2=y3')
pt.plot(w,np.abs(Y3),color='gold')
if(X3.all()==Y3.all()):
    print("linearity verified")
pt.show()