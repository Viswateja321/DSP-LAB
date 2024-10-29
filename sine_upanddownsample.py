import numpy as np
import librosa
import matplotlib.pyplot as plt

def resample_signal(signal, original_sr, sampling_factor):
    # Calculate the new sampling rate
    new_sr = int(original_sr * sampling_factor)
    
    if new_sr == original_sr:
        print("Sampling factor does not change the sample rate.")
        return signal, original_sr
    
    # Resample the signal
    resampled_signal = librosa.resample(signal, orig_sr=original_sr, target_sr=new_sr)
    
    return resampled_signal, new_sr

# Generate a sine wave with a higher frequency
duration = 1.0  # seconds
original_sr = 44100  # Original sampling rate (44.1 kHz)
t = np.linspace(0, duration, int(original_sr * duration), endpoint=False)
frequency = 440  # Frequency of the sine wave in Hz (A4 note, 440 Hz)
signal = 0.5 * np.sin(2 * np.pi * frequency * t)

# Resample the sine wave with a noticeable factor
sampling_factor =float(input("Enter sampling factor"))  # Downsampling by a factor of 4
resampled_signal, new_sr = resample_signal(signal, original_sr, sampling_factor)

# Output the new sampling rate and resampled signal shape
print(f"Original sampling rate: {original_sr}")
print(f"New sampling rate: {new_sr}")
print(f"Original signal shape: {signal.shape}")
print(f"Resampled signal shape: {resampled_signal.shape}")

# Plot the original and resampled signals
plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(t[:1000], signal[:1000], label="Original Signal")
plt.title("Original Sine Wave")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()

# Time array for the resampled signal
t_resampled = np.linspace(0, duration, len(resampled_signal), endpoint=False)

plt.subplot(2, 1, 2)
plt.plot(t_resampled[:1000], resampled_signal[:1000], label="Resampled Signal", color='orange')
plt.title("Resampled Sine Wave")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()

plt.tight_layout()
plt.show()

