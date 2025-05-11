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

    with open("pub.key", 'wb') as f:
        f.write(rho)
        for poly in t_compressed:
            for coeff in poly:
                f.write(int(coeff).to_bytes(2, 'little'))
    
    with open("priv.key", 'wb') as f:
        for poly in secret_key:
            for coeff in poly:
                f.write((int(coeff) % q).to_bytes(2, 'little'))