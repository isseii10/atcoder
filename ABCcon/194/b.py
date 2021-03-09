import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ans = INF
    for i in range(n):
        a = ab[i][0]
        for j in range(n):
            b = ab[j][1]
            if i == j:
                res = a + b
            else:
                res = max(a, b)
            ans = min(ans, res)
    print(ans)

        
if __name__ == '__main__':
    main()