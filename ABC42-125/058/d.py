import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353

def main():
    n, m = map(int, input().split())
    xs = list(map(int,input().split()))
    ys = list(map(int,input().split()))

    x_sum = 0
    for i in range(n):
        x_sum += xs[i]*(n-1-i) #自分より大なものの数だけ足され
        x_sum -= xs[i]*i #自分より小なものの数だけ引かれる
        x_sum %= MOD

    y_sum = 0
    for i in range(m):
        y_sum += ys[i]*(m-1-i) #自分より大なものの数だけ足され
        y_sum -= ys[i]*i #自分より小なものの数だけ引かれる
        y_sum %= MOD


    print(x_sum*y_sum % MOD)
if __name__ == '__main__':
    main()