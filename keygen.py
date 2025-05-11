from matrix import gen_random_matrix
from noise import gen_noise
from compression import compress_vector
import numpy as np
import secrets

d_t = 2
q = 3329
eta = 2

def poly_mul(a, b):
    res = np.convolve(a, b) % q
    result = np.zeros(256, dtype=int)

    for i in range(256):
        result[i] = res[i]
    for i in range(256, len(res)):
        result[i - 256] = (result[i - 256] - res[i]) % q

    return result


def multiply_matrix_vector(matrix, vector):
    k = len(vector)
    result = []
    for i in range(k):
        acc = np.zeros(256, dtype=int)
        for j in range(k):
            acc = (acc + poly_mul(matrix[i][j], vector[j])) % q
        result.append(acc)
    return np.array(result, dtype=object)

def key_gen(k=3):
    rho = secrets.token_bytes(32)  
    A = gen_random_matrix(k, rho)

    s = gen_noise(k, eta)
    e = gen_noise(k, eta)

    t = multiply_matrix_vector(A, s)
    for i in range(k):
        t[i] = (t[i] + e[i]) % q

    t_compressed = compress_vector(t, d_t)

    public_key = (t_compressed, rho)
    secret_key = s

    return public_key, secret_key
