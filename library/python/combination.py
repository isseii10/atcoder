MOD = 10**9 + 7
# 分かりやすいけど遅い
"""
def comb(n, r):
    n_p, r_inv, nr_inv = 1, 1, 1
    for i in range(1, n+1):
        n_p *= i % mod
    for i in range(1, r+1):
        r_inv *= pow(i, mod-2, mod) % mod
    for i in range(1, n-r+1):
        nr_inv *= pow(i, mod-2, mod) % mod
    return (n_p * r_inv % mod) * nr_inv % mod
"""


# for 一回でまとめる
def comb(n, r):
    res = 1
    for i in range(1, r+1):
        res = res*(n-i+1) % mod
        res = res*pow(i, mod-2, mod) % mod
    return res

# 前処理O(n)でcomb(n, r)をO(1)で計算する。
# 1 <= r <= n <= 10**7
# 使用例167 colorful blocks
MAX = 1000000
fac = [1] * (MAX + 1)
inv = [1] * (MAX + 1)
def COMinit():
    for j in range(1, MAX + 1):
        fac[j] = fac[j - 1] * j % MOD

    inv[MAX] = pow(fac[MAX], MOD - 2, MOD)
    for j in range(MAX)[::-1]:
        inv[j] = inv[j + 1] * (j + 1) % MOD

def COM(n, r):
    if r > n or n < 0 or r < 0:
        return 0
    return fac[n] * inv[n - r] * inv[r] % MOD


# mod使わない
# 遅いやつ
import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))