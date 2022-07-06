import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    a = []
    b = []
    time = []
    total_time = 0
    for _ in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
        time.append(ai / bi)
        total_time += ai / bi
    
    burn_time = total_time / 2
    ans = 0
    for i in range(n):
        if burn_time > time[i]:
            burn_time -= time[i]
            ans += a[i]
        else:
            ans += burn_time * b[i]
            break
    print(ans)






if __name__ == '__main__':
    main()