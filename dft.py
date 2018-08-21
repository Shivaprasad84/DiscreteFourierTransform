"""
Discrete Fourier Transform:

given a discrete time sequence x(n) the following program calculates the DFT X(k)
and presents the output in both rectangular and polar form.

Sample Input:

x(n): 1 1 0 0
N: 4 (N can be more than the length of x(n) for increased resolution.)

Sample Output:

X(K): [(2+0j), (1-1j), 0j, (1+1j)]
Polar Form: [[2.0, 0.0], [1.414214, -45.0], [0.0, 0.0], [1.414214, 45.0]]

"""
import math
import cmath

a = [complex(x) for x in input('x(n): ').strip().split(' ')] # x(n)
N = int(input('N: ')) # N
res = []

while(len(a) < N):
    a.append(0)
    
for K in range(N):
    d = complex(0, 0)
    for n in range(N):
        m = complex(math.cos(2*math.pi*K*n/N), -1*math.sin(2*math.pi*K*n/N))
        d += a[n]*complex(round(m.real, 2), round(m.imag, 2))
    res.append(d)
    
print("X(K): {}\n".format(res))
pol = [list(cmath.polar(x)) for x in res]

# for increased precision and angle in radians remove this for loop
for i in pol:
    i[0] = round(i[0], 6)
    i[1] = round(i[1]*180/math.pi, 2)

    
print("Polar Form: {}".format(pol))
