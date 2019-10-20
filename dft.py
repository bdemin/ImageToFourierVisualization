import numpy as np


def dft(x):
    # Discrete Fourier Transform (2D)

    X = []
    N = len(x)

    for k in range(N):
        _sum = complex(0,0)
        for n in range(N):
            phi = (2 * np.pi * k * n) / N
            c = complex(np.cos(phi), -np.sin(phi))
            xn = complex(x[n][0],x[n][1])
            _sum = _sum + (xn * c)
            
        _sum = complex(_sum.real / N, _sum.imag / N)

        freq = k
        amp = np.sqrt(_sum.real * _sum.real + _sum.imag * _sum.imag)
        phase = np.arctan2(_sum.imag, _sum.real)
        X.append({'freq': freq,
                'amp': amp,
                'phase': phase})
    X = sorted(X, key = lambda i: i['amp'], reverse = True) 
    return X
