import hashlib
import secrets

q = 3329

def gen_randon_pol(seed, i, j):
    seed_i_j = seed + (i).to_bytes(1, 'big') + (j).to_bytes(1, 'big')
    shake = hashlib.shake_128()
    shake.update(seed_i_j)
    pol = [0] * 256

    unfilled_coefficients = 0
    while unfilled_coefficients < 256:
        extracted_bytes = shake.digest(168)
        for t in range(84):
            d1 = extracted_bytes[2 * t]
            d2 = extracted_bytes[2 * t + 1]
            combined_bytes = (d1 << 8) + d2

            if combined_bytes < 19 * q:
                coef = combined_bytes % q
                pol[unfilled_coefficients] = coef
                unfilled_coefficients += 1

    return pol

def gen_randon_matrix(k):
    matrix = [[0] * k for _ in range(k)]
    seed = secrets.token_bytes(32)
    for i in range(k):
        for j in range(k):
            matrix[i][j] = gen_randon_pol(seed, i, j)

    return matrix