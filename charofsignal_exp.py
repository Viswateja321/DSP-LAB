import numpy as np
import matplotlib.pyplot as plt

# Given signal (you can replace this with your actual signal)
n = np.arange(0, 100)  # time index
x = np.sin(0.1 * np.pi * n)  # example signal (sine wave)

# Exponentially decreasing signal
alpha = 0.05  # rate of exponential decay
exp_decay = np.exp(-alpha * n)

# Resultant signal
resultant_signal = x * exp_decay

# Plotting the original and resultant signals
plt.figure(figsize=(10, 6))

# Plot original signal
plt.subplot(2, 1, 1)
plt.stem(n, x, 'b', basefmt=" ", use_line_collection=True)
plt.title("Original Signal")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)

# Plot resultant signal (after multiplication)
plt.subplot(2, 1, 2)
plt.stem(n, resultant_signal, 'r', basefmt=" ", use_line_collection=True)
plt.title("Signal after Multiplication with Exponentially Decreasing Signal")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)

# Show plots
plt.tight_layout()
plt.show()

