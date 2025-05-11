from matrix import gen_random_matrix
from noise import gen_noise
from compression import compress_vector
import numpy as np
import secrets

def poly_mul(a, b, q):
    res = np.convolve(a, b) % q
    result = np.zeros(256, dtype=int)

    for i in range(256):
        result[i] = res[i]
    for i in range(256, len(res)):
        result[i - 256] = (result[i - 256] - res[i]) % q

    return result


def multiply_matrix_vector(matrix, vector, q):
    k = len(vector)
    result = []
    for i in range(k):
        acc = np.zeros(256, dtype=int)
        for j in range(k):
            acc = (acc + poly_mul(matrix[i][j], vector[j], q)) % q
        result.append(acc)
    return np.array(result, dtype=object)

def key_gen(k, eta, q, d_t):
    rho = secrets.token_bytes(32)  
    matrix = gen_random_matrix(k, rho, q)

    s = gen_noise(k, eta)
    e = gen_noise(k, eta)

    t = multiply_matrix_vector(matrix, s, q)
    for i in range(k):
        t[i] = (t[i] + e[i]) % q

    t_compressed = compress_vector(t, d_t, q)

    public_key = (t_compressed, rho)
    secret_key = s

    return public_key, secret_key
