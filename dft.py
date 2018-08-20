"""
Discrete Fourier Transform:

given a discrete time sequence x(n) the following program calculates the DFT X(k)
and presents the output in both rectangular an polar form.

Sample Input:
x(n): 1, 1, 0, 0
N: 4 //(N can be more than the length of x(n) for increased resolution.)

Sample Output:
X(K): [(2+0j), (1-1j), 0j, (1+1j)]
Polar Form: [(2.0, 0.0), (1.4142135623730951, -0.7853981633974483), (0.0, 0.0), (1.4142135623730951, 0.7853981633974483)]

"""
import math
import cmath
a = [int(x) for x in input("x(n): ").strip().split(', ')]
N = int(input("N: "))
res = []
while(len(a) != N):
    a.append(0)
for K in range(N):
    d = complex(0, 0)
    for i in range(N):
        m = (complex(math.cos(2*math.pi*K*i/N), -1*math.sin(2*math.pi*K*i/N)))
        d += a[i]*complex(round(m.real, 2), round(m.imag, 2))
    res.append(d)
print("X(K): {}\n".format(res))
print("Polar Form: {}".format([cmath.polar(x) for x in res]))

