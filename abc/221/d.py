import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    login = defaultdict(int)
    for _ in range(n):
        a, b = map(int, input().split())
        login[a] += 1
        login[a+b] -= 1

    days = sorted(list(login.keys()))

    for i in range(len(days)-1):
        login[days[i+1]] += login[days[i]]
    
    #print(login)
    ans = [0]*(n+1)
    for i in range(len(days)-1):
        num = days[i+1] - days[i] #numは何日間
        ans[login[days[i]]] += num
    print(*ans[1:])
if __name__ == '__main__':
    main()