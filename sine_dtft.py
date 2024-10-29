import numpy as np
import matplotlib.pyplot as plt

def dtft(signal, N):
    """
    Compute the Discrete-Time Fourier Transform (DTFT) of a signal.

    Parameters:
    - signal: The input discrete-time signal (numpy array)
    - N: Number of points in the DTFT (frequency resolution)

    Returns:
    - omega: Array of normalized frequencies where the DTFT is computed
    - dtft_signal: The DTFT of the signal
    """
    omega = np.linspace(-np.pi, np.pi, N, endpoint=False)
    dtft_signal = np.array([np.sum(signal * np.exp(-1j * w * np.arange(len(signal)))) for w in omega])
    return omega, dtft_signal

# Generate a sine wave
duration = 1.0  # seconds
sampling_rate = 1000  # Sampling rate in Hz
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
frequency = 5  # Frequency of the sine wave in Hz
signal = 0.5 * np.sin(2 * np.pi * frequency * t)

# Perform DTFT
N = 2048  # Number of points in DTFT (frequency resolution)
omega, dtft_signal = dtft(signal, N)

# Plot magnitude spectrum
plt.figure(figsize=(14, 6))

plt.subplot(2, 1, 1)
plt.plot(omega, np.abs(dtft_signal))
plt.title("Magnitude Spectrum")
plt.xlabel("Normalized Frequency (radians/sample)")
plt.ylabel("Magnitude")
plt.grid()

# Plot phase spectrum
plt.subplot(2, 1, 2)
plt.plot(omega, np.angle(dtft_signal))
plt.title("Phase Spectrum")
plt.xlabel("Normalized Frequency (radians/sample)")
plt.ylabel("Phase (radians)")
plt.grid()

plt.tight_layout()
plt.show()

