import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353




def main():
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()

    ans = 1
    for i, num in enumerate(c):
        ans = ans * (num - i) % MOD
    
    print(ans)

        


if __name__ == '__main__':
    main()