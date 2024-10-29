'''import numpy as np
import matplotlib.pyplot as plt

# Step 1: Take inputs from the user
n=int(input("Enter no.of zeroes")
for i in range(n):
    
r = float(input("Enter the distance of the zero (r) from the origin: "))
w = float(input("Enter the angular distance (w in radians): "))

# Step 2: Compute H(z) using the formula z = r * e^(jw)
z = r * np.exp(1j * w)  # Using complex exponential form

# Step 3: Define a function H(z) for frequency response
def H(z):
    return z  # In this case, H(z) is the value of z directly

# Step 4: Convert H(z) into H(w) and calculate the magnitude spectrum over a range of frequencies
omega = np.linspace(-np.pi, np.pi, 1000)  # Frequency range from -π to π
H_w = H(r * np.exp(1j * omega))  # Compute H(w) for each frequency omega
magnitude_spectrum = np.abs(H_w)  # Magnitude of H(w)

# Step 5: Plot the magnitude spectrum
plt.figure(figsize=(8, 6))
plt.plot(omega, magnitude_spectrum)
plt.title("Magnitude Spectrum of Zero")
plt.xlabel("Frequency (ω in radians)")
plt.ylabel("Magnitude |H(ω)|")
plt.grid(True)
plt.show()'''

import numpy as np
import matplotlib.pyplot as plt

# Step 1: Take inputs for multiple zeros from the user
num_zeros = int(input("Enter the number of zeros: "))

zeros = []
for i in range(num_zeros):
    r = float(input(f"Enter the distance of zero {i+1} (r) from the origin: "))
    w = float(input(f"Enter the angular distance of zero {i+1} (w in radians): "))
    zx = r * np.exp(1j * w)  # Compute zero in complex form
    zeros.append(zx)

# Step 2: Define the combined frequency response H(z)
def H(zeros, omega):
    H_w = np.ones_like(omega, dtype=complex)  # Initialize as 1 for multiplication
    for z in zeros:
        H_w *= (omega - z)  # Each zero contributes to the frequency response
    return H_w

# Step 3: Compute the frequency response over a range of frequencies
omega = np.linspace(-np.pi, np.pi, 1000)  # Frequency range from -π to π
H_w = H(zeros, r * np.exp(1j * omega))  # Compute the frequency response
magnitude_spectrum = np.abs(H_w)  # Magnitude of H(omega)
phase_spectrum = np.angle(H_w)  # Phase of H(omega)

# Step 4: Plot the zeros on the complex plane, the magnitude spectrum, and the phase spectrum
plt.figure(figsize=(12, 10))

# Subplot 1: Plot the zeros on the complex plane
plt.subplot(3, 1, 1)
for z in zeros:
    plt.plot(np.real(z), np.imag(z), 'bo')  # Plot each zero
plt.title("Zeros on Complex Plane")
plt.xlabel("Real Part")
plt.ylabel("Imaginary Part")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)

# Subplot 2: Plot the magnitude spectrum
plt.subplot(3, 1, 2)
plt.plot(omega, magnitude_spectrum)
plt.title("Combined Magnitude Spectrum of Zeros")
plt.xlabel("Frequency (ω in radians)")
plt.ylabel("Magnitude |H(ω)|")
plt.grid(True)

# Subplot 3: Plot the phase spectrum
plt.subplot(3, 1, 3)
plt.plot(omega, phase_spectrum)
plt.title("Combined Phase Spectrum of Zeros")
plt.xlabel("Frequency (ω in radians)")
plt.ylabel("Phase (radians)")
plt.grid(True)

plt.tight_layout()
plt.show()

