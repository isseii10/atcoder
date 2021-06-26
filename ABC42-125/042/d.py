#from sys import setrecursionlimit
#setrecursionlimit(10**7)
from sys import stdin
input = stdin.readline
INF = float('inf')
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
    for j in range(MAX - 1, -1, -1):
        inv[j] = inv[j + 1] * (j + 1) % MOD

def COM(n, r):
    if r > n or n < 0 or r < 0:
        return 0
    return fac[n] * inv[n - r] * inv[r] % MOD

def main():
    h, w, a, b = map(int, input().split())
    COMinit()
    ans = 0
    for i in range(b, w):
        tmp = COM((h-a-1)+i, h-a-1)
        #print(i, tmp)
        tmp *= COM(w-1-i+(a-1), a-1)
        tmp %= MOD
        ans = (ans + tmp) % MOD
    print(ans)
if __name__ == '__main__':
    main()