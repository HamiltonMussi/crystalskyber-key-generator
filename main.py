from keygen import key_gen

if __name__ == "__main__":
    public_key, secret_key = key_gen()
    print("Public Key:", public_key)
    print("Secret Key:", secret_key)