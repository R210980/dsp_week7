import numpy as np
def circ_shift(x,m):
	N=len(x)
	y=[]
	for n in range(0,N):
		if((n-m)>=0):
			idx=(n-m)%N
		else:
			idx=N+(n-m)
		y.append(x[idx])
	return y
def circ_conv(x1,x2):
	z=[]
	a=x2[1:]
	x2r=[x2[0]]+a[::-1]
	for n in range(len(x1)):
		y=circ_shift(x2r,n)
		z.append(np.dot(x1,y))
	return z
def over_lap(x,h,N):
	M=len(h)
	L=N-M+1
	x_pad=np.concatenate((np.zeros(M-1),x))
	y=np.zeros(len(x)+M-1)
	for i in range(0,len(x),L):
		x_block=x_pad[i:i+N]
		y_block=circ_conv(x_block,h)
		y[i:i+L]=y_block[M-1:]
	return y
x1=[7,6,4,5,2,4,5,2,3]
h1=[1,2,3]
N=3
y1=over_lap(x1,h1,N)
print(y1)
		
		
	
