import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n, x = map(int, input().split())
    A = list(map(int, input().split()))
    ans = []
    for a in A:
        if a == x:continue
        ans.append(a)
    print(*ans)
if __name__ == '__main__':
    main()