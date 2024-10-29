import numpy as np
import matplotlib.pyplot as plt

# Define the user-defined signals
signal1 = np.array([1, 2, 3, 4])
signal2 = np.array([2.8, 4.5, 6.4, 8])

# Function to zero-pad the signal
def zero_pad(signal, pad_width):
    return np.pad(signal, (0, pad_width), mode='constant')

# Define the padding width
pad_width = 4

# Pad the signals
padded_signal1 = zero_pad(signal1, pad_width)
padded_signal2 = zero_pad(signal2, pad_width)

# Function to compute DFT manually
def compute_dft(signal):
    N = len(signal)
    dft = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            dft[k] += signal[n] * np.exp(-2j * np.pi * k * n / N)
    return dft

# Compute the DFT of the original and padded signals manually
dft_signal1 = compute_dft(signal1)
dft_signal2 = compute_dft(signal2)
dft_padded_signal1 = compute_dft(padded_signal1)
dft_padded_signal2 = compute_dft(padded_signal2)

# Plot the original and padded signals in time domain
plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
plt.stem(np.arange(len(signal1)), signal1, use_line_collection=True)
plt.title('Original Signal 1 (Time Domain)')
plt.xlabel('Sample')
plt.ylabel('Amplitude')

plt.subplot(2, 2, 2)
plt.stem(np.arange(len(signal2)), signal2, use_line_collection=True)
plt.title('Original Signal 2 (Time Domain)')
plt.xlabel('Sample')
plt.ylabel('Amplitude')

plt.subplot(2, 2, 3)
plt.stem(np.arange(len(padded_signal1)), padded_signal1, use_line_collection=True)
plt.title('Padded Signal 1 (Time Domain)')
plt.xlabel('Sample')
plt.ylabel('Amplitude')

plt.subplot(2, 2, 4)
plt.stem(np.arange(len(padded_signal2)), padded_signal2, use_line_collection=True)
plt.title('Padded Signal 2 (Time Domain)')
plt.xlabel('Sample')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()

# Plot the magnitude of the DFT of the original and padded signals
plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
plt.stem(np.arange(len(dft_signal1)), np.abs(dft_signal1), use_line_collection=True)
plt.title('DFT of Original Signal 1 (Magnitude)')
plt.xlabel('Frequency Bin')
plt.ylabel('Magnitude')

plt.subplot(2, 2, 2)
plt.stem(np.arange(len(dft_signal2)), np.abs(dft_signal2), use_line_collection=True)
plt.title('DFT of Original Signal 2 (Magnitude)')
plt.xlabel('Frequency Bin')
plt.ylabel('Magnitude')

plt.subplot(2, 2, 3)
plt.stem(np.arange(len(dft_padded_signal1)), np.abs(dft_padded_signal1), use_line_collection=True)
plt.title('DFT of Padded Signal 1 (Magnitude)')
plt.xlabel('Frequency Bin')
plt.ylabel('Magnitude')

plt.subplot(2, 2, 4)
plt.stem(np.arange(len(dft_padded_signal2)), np.abs(dft_padded_signal2), use_line_collection=True)
plt.title('DFT of Padded Signal 2 (Magnitude)')
plt.xlabel('Frequency Bin')
plt.ylabel('Magnitude')

plt.tight_layout()
plt.show()

