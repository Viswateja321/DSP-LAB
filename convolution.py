#convolution of two signals
import numpy as np
import matplotlib.pyplot as plt

def dtft(x, w):
    return np.sum(x * np.exp(-1j * w * np.arange(len(x))))

x1 = np.array([1, 2, 3, 4, 5])
x2 = np.array([6, 7, 8, 9, 10])

x_conv = np.convolve(x1, x2, mode='full')

w = np.linspace(0, 2 * np.pi, 100)

X1 = np.array([dtft(x1, wi) for wi in w])
X2 = np.array([dtft(x2, wi) for wi in w])

X_conv = np.array([dtft(x_conv, wi) for wi in w])

X_expected = X1 * X2

plt.plot(np.abs(X_conv), label='Convolved')
plt.plot(np.abs(X_expected), label='Expected')
plt.legend()
plt.show()
