import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    ans = 0
    s, t = map(int, input().split())
    for a in range(101):
        for b in range(101):
            for c in range(101):
                if a + b + c > s:continue
                if a*b*c <= t:
                    ans += 1
    print(ans)
if __name__ == '__main__':
    main()