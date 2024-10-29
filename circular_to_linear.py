import numpy as np
from matplotlib import pyplot as plt
def dft(x,N):
	X=[]
	for k in np.arange(0,N):
		s=0
		for n in np.arange(0,N):
			s=s+x[n]*np.exp(-1j*2*np.pi*n*k/N)
		X.append(s)
	return X
def idft(X,N):
	x=[]
	for n in np.arange(0,N):
		s=0
		for k in np.arange(0,N):
			s=s+X[k]*np.exp(1j*2*np.pi*n*k/N)
		d=s/N
		x.append(d)
	return x
x1=[1,2,3,4]
x2=[5,6,2]
x1_z=[1,2,3,4,0,0]
x2_z=[5,6,2,0,0,0]
X1=np.array(dft(x1_z,6))
X2=np.array(dft(x2_z,6))
X3=X1*X2
y=idft(X3,6)
print(np.real(y))

