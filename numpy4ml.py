import numpy as np

a = np.array([1, 2, 3, 4])
b = np.arange(1, 5, 2)

print(a, b)
print(a.shape, a.dtype, a.size)

c = np.eye(3)
d = np.ones((3, 3))
e = np.zeros((3, 3))
f = np.empty((3, 3))

print(c, d, e, f, sep='\n\n')

g = np.float64(2)
print(g)

h = np.complex128(1 + 2j)
print(h, h.real, h.imag)

p = np.arange(2, 6).reshape(2, 2)
q = np.arange(9, 1, -2).reshape(2, 2)
print(p+q, p-q, 2*p, p**2, p.dot(q), np.dot(p, q), sep='\n')

r1 = p.T
r2 = np.transpose(p)
print('r1 = r2: ', r1 == r2, sep='\n')

arr = np.arange(12)
a1, a11 = arr.reshape(2, 3, 2)
a2 = arr.reshape(2, 6)
a3 = arr.reshape(1, 12)
a4 = arr.reshape(12, 1)
print(a1, a11, a2, arr, a3, a4, sep='\n\n')
arr.resize(2, 6)
print('arr = a2: ', arr == a2, sep='\n')
# splitting,  stacking, slicing
x1, x2 = np.split(a2, 2, axis=0)
x3, x4 = np.split(a2, 2, axis=1)
print(x1, x2, x3, x4, sep='\n')

x5, x6 = np.vsplit(a2, 2)
x7, x8 = np.hsplit(a2, 2)
print('x1 = x5; ', x1 == x5, 'x3 = x7; ', x3 == x7, sep='\n')

p1 = np.vstack((x1, x2))  # vertical stack
p2 = np.hstack((x3, x4))  # horizontal stack
p3 = np.concatenate((x1, x2), axis=0)
p4 = np.concatenate((x3, x4), axis=1)
print(p1, p2, 'p1 = p2; ', p1 == p2, 'p1 = p3', p1 == p3,  sep='\n')

print(arr[1:5], arr[5:1:-1], arr[::-1], a2, a2[0][3::-2], a2[1][2:5], sep='\n')

z = np.linspace(1, np.pi, 10)
print(z)
