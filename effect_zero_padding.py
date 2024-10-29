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
x1=[1,2,3,4]
x2=[1,2,3,4,0,0]
x3=[1,2,3,4,0,0,0,0,0]
X1=dft(x1,4)
X2=dft(x2,6)
X3=dft(x3,9)
x1_mag=np.abs(X1)
x2_mag=np.abs(X2)
x3_mag=np.abs(X3)
plt.subplot(3,1,1)
plt.plot(x1_mag)
plt.subplot(3,1,2)
plt.plot(x2_mag)
plt.subplot(3,1,3)
plt.plot(x3_mag)
plt.show()
