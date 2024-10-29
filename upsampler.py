#example code for upsampler
x=[1,2,3,4,5,6]
y=[]
le=len(x)-1
l=4
r=l*le+1
for i in range(0,r):
	if(i%l==0):
		y.append(x[int(i/l)])
	else:
		y.append(0)

print(list(y))
