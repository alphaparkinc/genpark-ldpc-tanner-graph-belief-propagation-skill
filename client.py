"""Low-Density Parity-Check (LDPC) Tanner Graph Belief Propagation Engine.
100% Python Standard Library.
"""

import math

class LDPCCodec:
    """Low-Density Parity-Check (LDPC) Tanner graph message passing."""
    def __init__(self, H):
        self.H = H
        self.m = len(H)
        self.n = len(H[0])

    def decode_llr(self, received_llrs, max_iter=10):
        v_to_c = [[0.0] * self.m for _ in range(self.n)]
        c_to_v = [[0.0] * self.n for _ in range(self.m)]

        for j in range(self.n):
            for i in range(self.m):
                if self.H[i][j]:
                    v_to_c[j][i] = received_llrs[j]

        for it in range(max_iter):
            for i in range(self.m):
                connected_v = [j for j in range(self.n) if self.H[i][j]]
                for j in connected_v:
                    prod = 1.0
                    for j_other in connected_v:
                        if j_other != j:
                            val = math.tanh(0.5 * v_to_c[j_other][i])
                            prod *= val
                    prod = max(-0.999999, min(0.999999, prod))
                    c_to_v[i][j] = 2.0 * math.atanh(prod)

            total_llr = [received_llrs[j] for j in range(self.n)]
            for j in range(self.n):
                for i in range(self.m):
                    if self.H[i][j]:
                        total_llr[j] += c_to_v[i][j]
                        v_to_c[j][i] = received_llrs[j] + sum(c_to_v[i_o][j] for i_o in range(self.m) if self.H[i_o][j] and i_o != i)

            hard_bits = [1 if total_llr[j] < 0 else 0 for j in range(self.n)]
            syndrome = [sum(self.H[i][j] * hard_bits[j] for j in range(self.n)) % 2 for i in range(self.m)]
            if all(s == 0 for s in syndrome):
                return {"bits": hard_bits, "converged": True, "iterations": it + 1}

        return {"bits": hard_bits, "converged": False, "iterations": max_iter}
