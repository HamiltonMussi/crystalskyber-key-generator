from matrix import gen_random_matrix
from noise import gen_noise
from compression import compress_vector
import numpy as np

d_t = 2
q = 3329
eta = 2

def multiply_matrix_vector(matrix, vector):
    k = len(vector)
    result = []
    for i in range(k):
        acc = np.zeros(256, dtype=int)
        for j in range(k):
            acc = (acc + (matrix[i][j] * vector[j])) % q
        result.append(acc)
    return np.array(result, dtype=object)

def key_gen(k=3):
    public_matrix = gen_random_matrix(k)
    s = gen_noise(k, eta)
    e = gen_noise(k, eta)
    t = multiply_matrix_vector(public_matrix, s) + e
    t_compressed = compress_vector(t, d_t)
    
    return (t_compressed, public_matrix), s
