q = 3329

def compress_vector(vector, coeff_size):
    n = len(vector)
    compressed_vector = [0] * n
    for i in range(n):
        compressed_vector[i] = round((vector[i] * (2 ** coeff_size) + q/2) / q) % q

    return compressed_vector