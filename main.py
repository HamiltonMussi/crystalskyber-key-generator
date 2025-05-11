from keygen import key_gen


if __name__ == "__main__":
    public_key, secret_key = key_gen()
    t_compressed, rho = public_key

    print("Public Key (compressed t):", t_compressed)
    print("Seed rho:", rho.hex())
    print("Secret Key (s vector):", secret_key)