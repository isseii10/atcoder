import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    sunuke = [INF]*n
    for i in range(n):
        from_t = t[i]
        from_s = sunuke[i-1] + s[i-1]
        sunuke[i] = min(from_t, from_s)
    for i in range(n):
        from_t = t[i]
        from_s = sunuke[i-1] + s[i-1]
        sunuke[i] = min(from_t, from_s)
    
    for i in range(n):
        print(sunuke[i])
if __name__ == '__main__':
    main()