import math
import cmath

def dft(Xn, N):
    """
    Xn --> type: list, content: int or complex.
    N --> type: int.
    Returns the DFT of x(n) for N samples.
    """
    Xn = [complex(x) for x in Xn]
    result = []
    while(len(Xn) < N):
        Xn.append(0)

    for k in range(N):
        ft = complex(0, 0)
        for n in range(N):
            twiddle_factor = (complex(math.cos(2*math.pi*k*n/N), -1*math.sin(2*math.pi*k*n/N)))
            ft += Xn[n]*complex(round(twiddle_factor.real, 2), round(twiddle_factor.imag, 2))
        result.append(ft)
    return result


def idft(Xk, N):
    """
    Xk --> type: list, content: int or complex.
    N --> type: int.
    Returns the inverse DFT of x(k) i.e, the original x(n).
    """
    Xk = [complex(x) for x in Xk]
    result = []
    for n in range(N):
        ift = complex(0, 0)
        for k in range(N):
            twiddle_factor = complex(math.cos(2*math.pi*k*n/N), math.sin(2*math.pi*k*n/N))
            ift += Xk[k]*complex(round(twiddle_factor.real, 2), round(twiddle_factor.imag, 2))
        result.append(ift/N)
    return result


def polar(Xk):
    """
    Xk --> type: list, content: int or complex.
    Converts a list of rectangular co-ordinates into polar co-ordinates and returns the same.
    """
    Xk = [complex(x) for x in Xk]
    pol = [list(cmath.polar(x)) for x in Xk]
    for i in pol:
        i[0] = round(i[0], 6)
        i[1] = round(i[1]*180/math.pi, 2)
    return pol
