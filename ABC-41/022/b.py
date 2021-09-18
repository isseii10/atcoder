import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    visited = set()
    ans = 0
    for ai in a:
        if ai in visited:
            ans += 1
        visited.add(ai)
    print(ans)
if __name__ == '__main__':
    main()