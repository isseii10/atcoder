import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n, k = map(int, input().split())

    for _ in range(k):
        if n % 200 == 0:
            n //= 200
        else:
            n_str = str(n)
            n_str += '200'
            n = int(n_str)
    
    print(n)
if __name__ == '__main__':
    main()