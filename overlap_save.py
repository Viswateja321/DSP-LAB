import numpy as np
import matplotlib.pyplot as plt

def overlap_save_convolution(signal, kernel, segment_length):
    """
    Perform convolution using the overlap-save method in a simplified manner.

    Parameters:
    - signal: Input signal array
    - kernel: Convolution kernel array
    - segment_length: Length of each segment for processing

    Returns:
    - Convolved signal
    """
    kernel_length = len(kernel)
    num_segments = (len(signal) + segment_length - 1) // segment_length
    
    # Pad the kernel to match segment length
    padded_kernel = np.pad(kernel, (0, segment_length - kernel_length), 'constant')

    # Prepare for storing the results
    convolved_segments = []

    for i in range(num_segments):
        start = i * segment_length
        end = min(start + segment_length, len(signal))
        segment = signal[start:end]
        
        # Pad the current segment to match segment_length
        padded_segment = np.pad(segment, (0, segment_length - len(segment)), 'constant')
        
        # Convolve the padded segment with the padded kernel
        result = np.convolve(padded_segment, padded_kernel, mode='full')
        
        # Save the relevant part of the result
        convolved_segments.append(result[kernel_length - 1:])
    
    # Concatenate all segments and trim to the original signal length
    convolved_signal = np.concatenate(convolved_segments)
    convolved_signal = convolved_signal[:len(signal) + kernel_length - 1]

    return convolved_signal

# Example usage
if __name__ == "__main__":
    # Define a signal and kernel
    signal = np.sin(np.linspace(0, 4 * np.pi, 500))  # Example signal (sine wave)
    kernel = np.array([0.25, 0.5, 0.25])  # Example kernel (simple moving average filter)
    
    # Define segment length (must be greater than the length of the kernel)
    segment_length = 128
    
    # Perform convolution using overlap-save method
    convolved_signal = overlap_save_convolution(signal, kernel, segment_length)
    
    # Plot the original and convolved signals
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(signal, label='Original Signal')
    plt.title('Original Signal')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(convolved_signal, label='Convolved Signal', color='orange')
    plt.title('Convolved Signal (Overlap-Save)')
    plt.legend()

    plt.tight_layout()
    plt.show()

