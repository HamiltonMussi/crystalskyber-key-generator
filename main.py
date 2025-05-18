from models.kyber_versions import Kyber512, Kyber768, Kyber1024
from time import time

if __name__ == "__main__":
    kyber_start_time = time()

    kyber = Kyber512()
    kyber.save_keys()

    kyber_end_time = time()

    print("Kyber key generation time (seconds): ", kyber_end_time - kyber_start_time)
