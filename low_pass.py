'''import numpy as np
import matplotlib.pyplot as plt
duration=float(input("Enter duration of sinusoid signal as 1 or 2 secs: "))
fs=float(input("Enter sampling frequency of sinusoid signal: "))
f=float(input("Enter frequency of sinusoid signal"))
t_cont=np.arange(0,duration,1/(fs*10))
x_cont=np.sin(2*np.pi*f*t_cont)
t_samp=np.arange(0,duration,1/fs)
x_samp=np.sin(2*np.pi*f*t_samp)
plt.figure(figsize=(10,6))
plt.plot(t_cont,x_cont, label='Continuous-time signal', color='b')
plt.stem(t_samp, x_samp, linefmt='r-', markerfmt='ro', basefmt='k', label=f'Sampled Signal (fs={fs} Hz)')
plt.title(f'Sine Wave:, f={f}Hz, Sampled at fs={fs}Hz')
plt.xlabel('time (s)')
plt.ylabel('Amplitude')
plt.show()'''


import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft

# Step 1: Generate a continuous-time sine wave signal
def continuous_signal(t, A, f, phi):
    return A * np.sin(2 * np.pi * f * t + phi)

# Step 2: Sample the continuous-time signal
def sample_signal(t, A, f, phi):
    return continuous_signal(t, A, f, phi)

# Step 3: Compute the N-point DFT of the sampled signal
def compute_dft(signal, N):
    return fft(signal, N)

# Step 4: Create frequency vector F for the DFT
def frequency_vector(N, fs):
    return np.fft.fftfreq(N, d=1/fs)

# Step 5: Apply low-pass filter
def low_pass_filter(dft_signal, freqs, fc):
    filter_mask = np.abs(freqs) <= fc
    h_k = np.where(filter_mask, 1, 0)  # Create filter: 1 for frequencies below fc, 0 otherwise
    return dft_signal * h_k, h_k

# Main function
def plot_signal_dft_and_filter(fs, N, fc):
    # Time vector for continuous signal
    t_cont = np.arange(0, 1, 1/(fs*10))  # High resolution for continuous signal

    # Step 1: Generate the continuous-time sine wave (A=1, f=5Hz, phi=0)
    x_cont = continuous_signal(t_cont, 1.0, 5.0, 0)

    # Step 2: Generate sampled signal
    t_samp = np.arange(0, 1, 1/fs)  # Time vector for sampling at fs
    x_samp = sample_signal(t_samp, 1.0, 5.0, 0)

    # Step 3: Compute the N-point DFT
    dft_signal = compute_dft(x_samp, N)

    # Step 4: Create frequency vector
    freqs = frequency_vector(N, fs)

    # Step 5: Apply low-pass filter to the DFT signal
    filtered_dft_signal, h_k = low_pass_filter(dft_signal, freqs, fc)

    # Step 6: Plot the continuous-time signal, sampled signal, and DFT magnitude
    plt.figure(figsize=(12, 8))

    # Plot the continuous-time signal
    plt.subplot(4, 1, 1)
    plt.plot(t_cont, x_cont, label='Continuous-Time Signal', color='b')
    plt.title('Continuous-Time Sine Wave (5 Hz)')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.grid(True)

    # Plot the sampled signal
    plt.subplot(4, 1, 2)
    plt.stem(t_samp, x_samp, linefmt='r-', markerfmt='ro', basefmt='k', label=f'Sampled Signal at fs={fs} Hz')
    plt.title(f'Sampled Signal at fs={fs} Hz')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.grid(True)

    # Plot the DFT magnitude
    plt.subplot(4, 1, 3)
    plt.plot(freqs[:N//2], np.abs(dft_signal[:N//2]), label='DFT Magnitude')
    plt.title('DFT Magnitude Spectrum')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Magnitude')
    plt.grid(True)

    # Step 7: Plot the low-pass filtered signal (h(k))
    plt.subplot(4, 1, 4)
    plt.stem(freqs[:N//2], h_k[:N//2], linefmt='g-', markerfmt='go', basefmt='k', label='Low-Pass Filter h(k)')
    plt.title(f'Low-pass Filter h(k) (fc={fc} Hz)')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('h(k)')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

    # Inverse DFT to get the filtered signal in the time domain
    filtered_signal = ifft(filtered_dft_signal).real

    # Step 8: Plot the filtered signal in the time domain
    plt.figure(figsize=(6, 4))
    plt.plot(t_samp, filtered_signal[:len(t_samp)], label='Filtered Signal in Time Domain')
    plt.title('Filtered Signal in Time Domain')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()

# User inputs
fs = float(input("Enter the sampling frequency (Hz): "))  # Sampling frequency
N = int(input("Enter the number of DFT points (N): "))    # Number of DFT points
fc = float(input("Enter the cutoff frequency for the low-pass filter (Hz): "))  # Low-pass filter cutoff frequency

# Call the main function
plot_signal_dft_and_filter(fs, N, fc)

