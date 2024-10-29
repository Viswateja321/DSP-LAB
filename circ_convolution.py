import numpy as np

def circular_convolution(x, h):
    # Length of the signals
    N = max(len(x), len(h))

    # Zero-padding to match the lengths of both signals
    x = np.pad(x, (0, N - len(x)), 'constant')
    h = np.pad(h, (0, N - len(h)), 'constant')

    # Initialize the result array
    y = np.zeros(N)

    # Compute circular convolution
    for n in range(N):
        for m in range(N):
            y[n] += x[m] * h[(n - m) % N]

    return y

# Get user input for the signals
x = list(map(float, input("Enter the values for the first signal x (comma-separated): ").split(',')))
h = list(map(float, input("Enter the values for the second signal h (comma-separated): ").split(',')))

# Convert lists to numpy arrays
x = np.array(x)
h = np.array(h)

# Calculate circular convolution
circular_conv_result = circular_convolution(x, h)

print("\nSignal x:", x)
print("Signal h:", h)
print("Circular Convolution Result:", circular_conv_result)

