import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n, z, w = map(int, input().split())
    A = list(map(int, input().split()))
    
    #最後のカードは必ずどちらかが持っている
    if n == 1:
        ans = abs(A[-1] - w)
    else:
        ans = max(abs(A[-1]-w), abs(A[-1]-A[-2]))
    print(ans)
if __name__ == '__main__':
    main()