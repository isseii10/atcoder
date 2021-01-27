import sys

input = sys.stdin.readline
#sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353

# for 一回でまとめる
def comb(n, r):
    res = 1
    for i in range(1, r+1):
        res = res*(n-i+1) % mod
        res = res*pow(i, mod-2, mod) % mod
    return res

def main():
    n, m = map(int, input().split())
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))
    unit_rect_sum = (xs[-1]-xs[0]) * (ys[-1] - ys[0]) % MOD
    print(unit_rect_sum * rect_nums % MOD)
    
    
if __name__ == '__main__':
    main()