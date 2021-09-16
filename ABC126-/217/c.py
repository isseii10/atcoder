import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    p = list(map(int, input().split()))

    q = [-1]*n
    for i, pi in enumerate(p):
        q[pi-1] = i+1

    print(*q)    
if __name__ == '__main__':
    main()