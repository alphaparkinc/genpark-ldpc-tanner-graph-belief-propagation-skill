from client import LDPCCodec

H = [
    [1, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 0],
    [1, 0, 1, 0, 0, 1]
]
ldpc = LDPCCodec(H)
llrs = [-2.0, -1.8, -2.2, 2.5, 2.1, 1.9]
res = ldpc.decode_llr(llrs, max_iter=5)
print(f"LDPC Decode Result: Converged={res['converged']}, Iterations={res['iterations']}, Bits={res['bits']}")
