import librosa
import scipy.signal
import numpy as np

def resample_audio(file_path, sampling_factor):
    # Load the audio file
    signal, original_sr = librosa.load(file_path, sr=None)
    
    # Calculate the new sampling rate
    new_sr = int(original_sr * sampling_factor)
    
    # Resample the audio signal
    if sampling_factor < 1:
        # Upsampling
        resampled_signal = librosa.resample(signal, orig_sr=original_sr, target_sr=new_sr)
    elif sampling_factor > 1:
        # Downsampling
        resampled_signal = librosa.resample(signal, orig_sr=original_sr, target_sr=new_sr)
    else:
        # No resampling
        resampled_signal = signal
    
    return resampled_signal, new_sr

# Example usage:
file_path = '/home/likitha/Downloads/audio-logo-little-rascal-185093.mp3'
sampling_factor = float(input("Enter sampling factor"))  # Less than 1 for upsampling, greater than 1 for downsampling
resampled_signal, new_sr = resample_audio(file_path, sampling_factor)

# Output the new sampling rate and resampled signal
print(f"New sampling rate: {new_sr}")
print(f"Resampled signal : {resampled_signal.shape}")
