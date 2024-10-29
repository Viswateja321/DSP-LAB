#Effect of zero padding on audio signal with different sampling rates
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import resample

def load_audio(file_path):
    """Load an audio file and return the sampling rate and data."""
    rate, data = wavfile.read(file_path)
    return rate, data

def zero_pad(signal, target_length):
    """Zero pad a signal to the target length."""
    padding_length = target_length - len(signal)
    if padding_length > 0:
        return np.pad(signal, (0, padding_length), 'constant')
    else:
        return signal[:target_length]

def resample_signal(signal, original_rate, target_rate):
    """Resample the signal to a new sampling rate."""
    number_of_samples = int(len(signal) * float(target_rate) / original_rate)
    return resample(signal, number_of_samples)

def plot_signals(signals, labels):
    """Plot the signals for comparison."""
    plt.figure(figsize=(12, 8))
    for i, signal in enumerate(signals):
        plt.plot(signal, label=labels[i])
    plt.xlabel('Sample Index')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.title('Effect of Zero Padding on Audio Signal with Different Sampling Rates')
    plt.show()

# Load audio file
file_path = '/home/likitha/Downloads/mixkit-small-group-cheer-and-applause-518.wav'  # Replace with your file path
original_rate, data = load_audio(file_path)

# Define different target sampling rates (example: original rate, half, double)
target_rates = [original_rate, original_rate // 2, original_rate * 2]

# Resample the signal to different rates and apply zero padding
padded_signals = []
for rate in target_rates:
    resampled_data = resample_signal(data, original_rate, rate)
    padded_data = zero_pad(resampled_data, len(data) * 4)  # Pad to 4 times the original length
    padded_signals.append(padded_data)

# Plot the original and zero-padded signals
plot_signals(
    padded_signals,
    [f'Rate {rate} Hz, Padded' for rate in target_rates]
)
