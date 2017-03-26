import numpy as np
np.random.seed(5)

x1 = np.random.randint(10, size = 6)
x2 = np.random.randint(10, size = (3,4))
x3 = np.random.randint(10, size = (3,4,5))

print(x1)
print(x2)
print(x3)

print('size', x3.size)
print('dim', x3.ndim)
print('shape', x3.shape)
print('dtype', x3.dtype)


x4 = [1,2,3,4,5]
print('1',x4[0])
print('5',x4[-1])
print('4',x4[-2])

x5 = np.array([[1,2,3,4,5],[2,4,6,8,0]])
print(x5)
print(x5[0,2])

x5[0,2] = 999
print(x5)

x6 = [i for i in range(20)]
print(type(x6))

x6 = np.array([i for i in range(20)])
print(type(x6))

print(x6[::2])
print(x6[::-1])

x7 = np.array([[1,2,3,4,5],[2,4,6,8,0]])
print(x7)
print(x7[0,:])
print(x7[:,1])


grid = np.arange(1,10)
print(grid)
print(grid.reshape(3,3))

# row vector
print(grid[np.newaxis,:])

# col vector
print(grid[:,np.newaxis])


















