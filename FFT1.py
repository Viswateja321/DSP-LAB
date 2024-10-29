'''import numpy as np

def fft(x):
    N = len(x)
    if N <= 1:
        return x

    # Divide
    even = fft(x[0::2])
    odd = fft(x[1::2])

    # Conquer
    T = [np.exp(-2j * np.pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]

# Example usage
if _name_ == "_main_":
    # Sample input (can be any 1D complex or real signal)
    x = np.random.random(8)  # Example: a random array of 8 points
    print("Input:", x)
    result = fft(x)
    print("FFT Result:", result)'''
import numpy as np

def fft(x):
    N = len(x)
    if N <= 1:
        return x

    # Divide the input into even and odd indexed elements
    even = fft(x[0::2])
    odd = fft(x[1::2])

    # Combine results
    T = [np.exp(-2j * np.pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]

# Example usage
if _name_ == "_main_":
    x = np.array([1, 2, 3, 4, 0, 0, 0, 0])  # Example input (length must be a power of 2)
    print("Input:", x)
    result = fft(x)
    print("FFT Result:", result)
