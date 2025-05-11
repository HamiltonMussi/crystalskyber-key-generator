import numpy as np

q = 3329

def compress_vector(vector, coeff_size):
    n = len(vector)
    compressed_vector = np.zeros(n, dtype=object)
    
    for i in range(n):
        pol = vector[i]
        compressed_pol = np.zeros(256, dtype=int)
        
        for j in range(256):
            compressed_pol[j] = int(round((pol[j] * (2 ** coeff_size) + q/2) / q)) % (2 ** coeff_size)
        
        compressed_vector[i] = compressed_pol

    return compressed_vector