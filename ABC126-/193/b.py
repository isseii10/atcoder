import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    pax = []
    for _ in range(n):
        a, p, x = map(int, input().split())
        pax.append((p, a, x))
    pax.sort()
    ans = -1
    for p, a, x in pax:
        if a >= x:continue
        ans = p
        break
    print(ans)

    
if __name__ == '__main__':
    main()