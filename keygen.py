from matrix import gen_randon_matrix
from noise import gen_noise
from compression import compress_vector

def key_gen(k=3):
    public_matrix = gen_randon_matrix(k)
    s = gen_noise(k, mu=2)
    e = gen_noise(k, mu=2)
    t = public_matrix @ s + e
    t_compressed = compress_vector(t, d_t=2)
    
    return (t_compressed, public_matrix), s
