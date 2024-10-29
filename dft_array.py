#python program to perform dft on an array signal and plot magnitude and phase spectrum
import numpy as np
import matplotlib.pyplot as plt

# Function to compute DFT
def DFT(x):
    N = len(x)
    X = np.zeros(N, dtype=complex)  # Initialize the result array with zeros (complex type)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
    return X

# Example signal array
x = np.array([1, 2, 3, 4, 2, 1])

# Compute DFT using the custom function
X = DFT(x)

# Compute magnitude and phase spectra
magnitude_spectrum = np.abs(X)
phase_spectrum = np.angle(X)

# Plot the magnitude spectrum
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.stem(np.arange(len(X)), magnitude_spectrum, use_line_collection=True)
plt.title("Magnitude Spectrum")
plt.xlabel("Frequency Bin")
plt.ylabel("Magnitude")

# Plot the phase spectrum
plt.subplot(1, 2, 2)
plt.stem(np.arange(len(X)), phase_spectrum, use_line_collection=True)
plt.title("Phase Spectrum")
plt.xlabel("Frequency Bin")
plt.ylabel("Phase (radians)")

plt.tight_layout()
plt.show()
