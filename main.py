from models.kyber import Kyber
from time import time

if __name__ == "__main__":
    k = 2  
    eta = 2
    q = 3329
    d_t = 11

    kyber_start_time = time()

    kyber = Kyber(k, eta, q, d_t)
    kyber.save_keys()

    kyber_end_time = time()

    print("Kyber key generation time (seconds): ", kyber_end_time - kyber_start_time)
