import sys
from typing import Counter

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353

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


def main():
    n = int(input())
    c = list(map(int, input().split()))
    c_count = Counter(c)
    c_list = []
    for k, v in c_count.items():
        c_list.append([k, v])
    c_list.sort()

    ans = 1
    used = 0
    for k, v in c_list:
        used += v
        


if __name__ == '__main__':
    main()