import numpy as np
import matplotlib.pyplot as plt

def dtft(x, w):
    return np.sum(x * np.exp(-1j * w * np.arange(len(x))))

x = np.array([1, 2, 3, 4, 5])

w = np.linspace(0, 2 * np.pi, 100)
X = np.array([dtft(x, wi) for wi in w])

R_X = np.array([np.sum(X * np.conj(X) * np.exp(1j * wi * np.arange(len(X)))) for wi in w])

X_autocorrelated = np.array([dtft(x, wi) * np.conj(dtft(x, wi)) for wi in w])

plt.plot(np.abs(X), label='DTFT')
plt.plot(np.abs(R_X), label='Autocorrelated DTFT')
plt.plot(np.abs(X_autocorrelated), label='Expected')
plt.legend()
plt.show()
