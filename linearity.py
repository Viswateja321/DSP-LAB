import numpy as np
import matplotlib.pyplot as plt

# Define the DTFT function
def dtft(x, n, omega):
    X = np.zeros_like(omega, dtype=complex)
    for i, w in enumerate(omega):
        X[i] = np.sum(x * np.exp(-1j * w * n))
    return X

# Parameters
n = np.arange(0, 100, 1)  # Discrete time indices
omega = np.linspace(-np.pi, np.pi, 1000)  # Frequency range

# Define two signals
x = np.sin(2 * np.pi * 0.1 * n)  # First signal
y = np.cos(2 * np.pi * 0.1 * n)  # Second signal

# Define constants
a = 2
b = 3

# Compute DTFT of individual signals
X = dtft(x, n, omega)
Y = dtft(y, n, omega)

# Compute DTFT of the linear combination
x_combined = a * x + b * y
X_combined = dtft(x_combined, n, omega)

# Compute linear combination of DTFTs
combined_dtft = a * X + b * Y

# Plot results
plt.figure(figsize=(12, 8))

# Plot DTFT of combined signal
plt.subplot(2, 2, 1)
plt.plot(omega, np.abs(X_combined))
plt.title('Magnitude of DTFT of Combined Signal')
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('Magnitude')

plt.subplot(2, 2, 2)
plt.plot(omega, np.angle(X_combined))
plt.title('Phase of DTFT of Combined Signal')
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('Phase (radians)')

# Plot linear combination of DTFTs
plt.subplot(2, 2, 3)
plt.plot(omega, np.abs(combined_dtft))
plt.title('Magnitude of Linear Combination of DTFTs')
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('Magnitude')

plt.subplot(2, 2, 4)
plt.plot(omega, np.angle(combined_dtft))
plt.title('Phase of Linear Combination of DTFTs')
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('Phase (radians)')

plt.tight_layout()
plt.show()
