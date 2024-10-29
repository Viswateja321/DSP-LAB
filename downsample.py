l=[]
n=int (input("ENter no.of samples in a time interval"))
print("enter the discrete data ")
for i in range(0,n):
    k=int(input())
    l.append(k)
a=int( input("Enter your scaling factor"))
def downsample(l1,a):
    if a>1:
        l2=[]
        for i in range (0,len(l1),a):
                l2.append(l1[i])
        return l2
    else:
        return l1
print("downsampled signal", downsample(l,a))
