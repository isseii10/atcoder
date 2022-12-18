from collections import defaultdict
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    s = input()[:-1]
    n = len(s)
    k = int(input())
    count_dot = [0]*(n+1)
    ans = 0
    for i in range(n):
        if s[i] == ".":
            count_dot[i+1] = count_dot[i] + 1
        else:
            count_dot[i+1] = count_dot[i]
    r = 0
    for l in range(n):
        while r < n and count_dot[r+1] - count_dot[l] <= k:
            r += 1
        ans = max(ans, r-l)
    print(ans)
if __name__ == '__main__':
    main()