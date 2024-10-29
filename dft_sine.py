#python code to perform dft on sinusoid signal and find k and verify the peak value
'''import numpy as np
import matplotlib.pyplot as plt

def DFT(x):
    N = len(x)
    X = np.zeros(N, dtype=complex)  # Initialize the result array with zeros (complex type)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
    return X

# Parameters for the sinusoidal signal
Fs = 1000   # Sampling frequency (samples per second)
T = 1       # Duration in seconds
f = 5       # Frequency of the sinusoid (Hz)
N = Fs * T  # Total number of samples (1000)

# Generate the sinusoidal signal
t = np.linspace(0, T, N, endpoint=False)
x = np.sin(2 * np.pi * f * t)

# Perform DFT on the signal
X = DFT(x)

# Compute the magnitude and phase spectra
magnitude_spectrum = np.abs(X)
phase_spectrum = np.angle(X)

# Find the peak value in the magnitude spectrum
peak_index = np.argmax(magnitude_spectrum)
peak_value = magnitude_spectrum[peak_index]

# Verify the frequency corresponding to the peak value
peak_frequency = peak_index * Fs / N

# Output the peak value and corresponding frequency
print(f"Peak magnitude value: {peak_value}")
print(f"Frequency corresponding to peak: {peak_frequency} Hz")

# Plotting the original signal, magnitude spectrum, and phase spectrum
plt.figure(figsize=(18, 8))

# Plot the original sinusoidal signal
plt.subplot(1, 3, 1)
plt.plot(t, x)
plt.title("Original Sinusoidal Signal")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")

# Plot the magnitude spectrum
plt.subplot(1, 3, 2)
plt.stem(np.arange(N) * Fs / N, magnitude_spectrum, use_line_collection=True)
plt.title("Magnitude Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.xlim(0, Fs / 2)  # Plot only up to the Nyquist frequency

# Plot the phase spectrum
plt.subplot(1, 3, 3)
plt.stem(np.arange(N) * Fs / N, phase_spectrum, use_line_collection=True)
plt.title("Phase Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase (radians)")
plt.xlim(0, Fs / 2)  

plt.tight_layout()
plt.show()'''


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

# Parameters for the sinusoidal signal
Fs = 1000  # Sampling frequency (samples per second)
N = 1000   # Total number of samples
T = 2 * np.pi  # Duration in terms of the signal's period

# Generate the sinusoidal signal from pi to -pi
t = np.linspace(np.pi, -np.pi, N, endpoint=False)
f = 5  # Frequency of the sinusoid (arbitrary since we're defining over a specific interval)
x = np.sin(f * t)

# Perform DFT on the signal
X = DFT(x)

# Compute the magnitude and phase spectra
magnitude_spectrum = np.abs(X)
phase_spectrum = np.angle(X)

# Find the peak value in the magnitude spectrum
peak_index = np.argmax(magnitude_spectrum)
peak_value = magnitude_spectrum[peak_index]

# Verify the frequency corresponding to the peak value
peak_frequency = peak_index * Fs / N

# Output the peak value and corresponding frequency
print(f"Peak magnitude value: {peak_value}")
print(f"Frequency corresponding to peak: {peak_frequency} Hz")

# Plotting the original signal, magnitude spectrum, and phase spectrum
plt.figure(figsize=(18, 8))

# Plot the original sinusoidal signal
plt.subplot(1, 3, 1)
plt.plot(t, x)
plt.title("Original Sinusoidal Signal")
plt.xlabel("Time (radians)")
plt.ylabel("Amplitude")

# Plot the magnitude spectrum
plt.subplot(1, 3, 2)
plt.stem(np.arange(N) * Fs / N, magnitude_spectrum, use_line_collection=True)
plt.title("Magnitude Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.xlim(0, Fs / 2)  # Plot only up to the Nyquist frequency

# Plot the phase spectrum
plt.subplot(1, 3, 3)
plt.stem(np.arange(N) * Fs / N, phase_spectrum, use_line_collection=True)
plt.title("Phase Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase (radians)")
plt.xlim(0, Fs / 2)  # Plot only up to the Nyquist frequency

plt.tight_layout()
plt.show()


