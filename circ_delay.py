import numpy as np

def cyclic_delay(signal, delay):
    n = len(signal)
    delay = delay % n  # Ensures the delay wraps around
    return np.concatenate((signal[-delay:], signal[:-delay]))

# Example usage
signal = np.array([1, 2, 3, 4, 5])  # Original signal
delay = 2  # Delay by 2 steps

#delayed_signal = cyclic_delay(signal, delay)
print("Original signal:", signal)
print("Delayed signal:", delayed_signal)
