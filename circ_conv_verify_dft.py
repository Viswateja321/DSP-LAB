import numpy as np

def dft(x):
    N = len(x)
    X = np.zeros(N, dtype=np.complex128)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
    return X

def idft(X):
    N = len(X)
    x = np.zeros(N, dtype=np.complex128)
    for n in range(N):
        for k in range(N):
            x[n] += X[k] * np.exp(2j * np.pi * k * n / N)
        x[n] /= N
    return x.real


def circular_convolution(x, h):
    N = len(h)
    x_padded = np.pad(x, (0, N - len(x)))  # Pad x with zeros
    X = dft(x_padded)
    H = dft(h)
    Y = X * H
    y = idft(Y)
    return y


x = np.array([8, 0, 1, 9, 6])
h = np.array([0, 7, 0, 5, 6])

X1= dft(x)
X2= dft(h)

y= idft(X1*X2)
Y= circular_convolution(x, h)

print("Circular Convolution:", y)
print("direct method Circular convolution :", Y)

if y.all()==Y.all():
	print("circular convolution is verified")
else:
	print("Circular convolution is not verified")
