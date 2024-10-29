import cmath
import numpy as np

# Recursive implementation of the Cooley-Tukey FFT algorithm
def fft(signal):
    N = len(signal)
    
    # Base case: if the input length is 1, just return the input
    if N == 1:
        return signal
    
    # Divide: split the signal into even and odd parts
    even = fft(signal[0::2])
    odd = fft(signal[1::2])
    
    # Initialize an array to hold the FFT result
    result = [0] * N
    
    # Combine: use the FFT of the even and odd parts to compute the FFT of the original signal
    for k in range(N // 2):
        t = cmath.exp(-2j * cmath.pi * k / N) * odd[k]
        result[k] = even[k] + t
        result[k + N // 2] = even[k] - t
    
    return result

# Test the FFT implementation
if __name__ == "__main__":
    # Example signal (real part of a sine wave)
    signal = [0.0, 1.0, 0.0, -1.0]  # You can replace this with any signal
    
    # Perform FFT
    fft_result = fft(signal)
    
    # Display the result
    print("FFT result:")
    for value in fft_result:
        print(f"{value:.4f}")

