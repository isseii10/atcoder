import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    ans = n
    seen = set()
    for i in range(2, int(n**(0.5)) + 10):
        tmp = i
        tmp *= i
        res = 0
        while tmp <= n:
            if tmp not in seen:
                res += 1
            seen.add(tmp)
            tmp *= i
        ans -= res
    print(ans)
        

if __name__ == '__main__':
    main()