import dsp

Xn = [complex(x) for x in input('x(n): ').strip().split(', ')]
N = int(input('N: '))

# Discrete fourier transform:
Xk = dsp.dft(Xn, N)
print('X(k):       {}'.format(Xk))

# Polar form of Xk:
pol = dsp.polar(Xk)
print('Polar Form: {}'.format(pol))

# Inverse discrete fourier transform:
Xn = dsp.idft(Xk, N)
print('Idft:       {}'.format(Xn))
