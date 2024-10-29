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
def overlap_add(x, h, N):
    M = len(h)
    L = N - M + 1  
    x_padded = np.concatenate((x, np.zeros(N - len(x) % N)))  
    num_blocks = len(x_padded) // L

    y = np.zeros(len(x_padded) + M - 1)
    
    for i in range(num_blocks):
        start = i * L
        end = start + N
        x_block = x_padded[start:end]
        
        x_block_padded = np.concatenate((x_block, np.zeros(M - 1)))
        
        y_block =circ_conv(x_block_padded, h)
        
        y[start:start + N + M - 1] += y_block
        
    return y[:len(x)]
x1=[1,2,3,4,5,6,7,8]
h1=[1,1,1]
N=4
y1=overlap_add(x1,h1,N)
print(y1)

