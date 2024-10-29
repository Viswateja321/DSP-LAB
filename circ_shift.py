#python program to circular shift the user entered signal
'''import numpy as np

def circular_shift(signal, shift):
    N = len(signal)
    # Compute the circularly shifted signal
    shifted_signal = np.zeros(N)
    for i in range(N):
        shifted_signal[i] = signal[(i - shift) % N]
    return shifted_signal

# Input the signal from the user
signal_input = input("Enter the signal (space-separated): ").split()
signal = np.array([float(x) for x in signal_input])

# Input the shift amount from the user
shift = int(input("Enter the shift amount: "))

# Perform circular shift
shifted_signal = circular_shift(signal, shift)

# Output the result
print("Original Signal: ", signal)
print("Shifted Signal: ", shifted_signal)'''
import numpy as np
def circ_shift(sig,m):
    N=len(sig)
    y=[]
    for i in range(0,N):
        if i-m>=0:
            idx=(i-m)%N
        else:
            idx=N+(i-m)
        y.append(sig[int(idx)])
    return y
sig=[]
l=int(input("Enter the signal length"))
for i in range(l):
    a=float(input("Enter amplitude"))
    sig.append(a)
print("Original signal:", sig)
m=float(input("Enter shifting value"))
shifted=circ_shift(sig,m)
print("Shifted signal: ", shifted)

            

