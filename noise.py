import random

def gen_noise(size, mu):
    noise_vector = [0] * size
    for i in range(size):
        noise = 0
        for _ in range(mu):
            bit_a = random.getrandbits(1)
            bit_b = random.getrandbits(1)
            diff = bit_a - bit_b
            noise += diff

        noise_vector[i] = noise

    return noise_vector