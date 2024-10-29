import numpy as np
import matplotlib.pyplot as plt

def overlap_add_convolution(signal, kernel, segment_length):
    """
    Perform convolution using the overlap-add method.

    Parameters:
    - signal: Input signal array
    - kernel: Convolution kernel array
    - segment_length: Length of each segment for processing

    Returns:
    - Convolved signal
    """
    kernel_length = len(kernel)
    output_length = len(signal) + kernel_length - 1
    num_segments = (len(signal) + segment_length - 1) // segment_length
    
    # Prepare the output signal
    convolved_signal = np.zeros(output_length)
    
    for i in range(num_segments):
        start = i * segment_length
        end = min(start + segment_length, len(signal))
        segment = signal[start:end]
        
        # Convolve the current segment with the kernel
        segment_result = np.convolve(segment, kernel)
        
        # Add the result to the output signal with overlap
        convolved_signal[start:start + len(segment_result)] += segment_result
    
    return convolved_signal

# Example usage
if __name__ == "__main__":
    # Define a signal and kernel
    signal = np.sin(np.linspace(0, 4 * np.pi, 500))  # Example signal (sine wave)
    kernel = np.array([0.25, 0.5, 0.25])  # Example kernel (simple moving average filter)
    
    # Define segment length (must be smaller than the signal length)
    segment_length = 128
    
    # Perform convolution using overlap-add method
    convolved_signal = overlap_add_convolution(signal, kernel, segment_length)
    
    # Plot the original and convolved signals
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(signal, label='Original Signal')
    plt.title('Original Signal')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(convolved_signal, label='Convolved Signal', color='orange')
    plt.title('Convolved Signal (Overlap-Add)')
    plt.legend()

    plt.tight_layout()
    plt.show()

