import numpy as np

def poly_mul(a, b, q):
    result = np.zeros(256, dtype=int)
    
    for i in range(256):
        for j in range(256):
            if i + j < 256:
                result[(i + j) % 256] = (result[(i + j) % 256] + a[i] * b[j]) % q
            else:
                result[(i + j) % 256] = (result[(i + j) % 256] - a[i] * b[j]) % q
                
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