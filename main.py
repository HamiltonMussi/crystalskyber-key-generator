from keygen import key_gen

# Parameters definition (Kyber-512)
k = 2  
eta = 2
q = 3329
d_t = 11

if __name__ == "__main__":
    public_key, secret_key = key_gen(k, eta, q, d_t)
    t_compressed, rho = public_key

    print("Public Key (compressed t):", t_compressed)
    print("Seed rho:", rho.hex())
    print("Secret Key (s vector):", secret_key)