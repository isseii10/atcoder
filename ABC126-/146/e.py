import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, m = map(int, input().split())
    s = input()[:-1]
    res = deque()

    def dfs(now):
        jump = -1
        for j in range(1, m+1)[::-1]:
            if now - j >= 0 and s[now - j] == "0":
                jump = j
                break
        else:
            # "1"が連続m個ある区間があるのでFalseを返す
            return False

        #jump先があるので、答えに追加
        res.appendleft(jump)
    
        if now-jump == 0:
            return True

        return dfs(now-jump)

    ok = dfs(n)
    if ok:
        print(*res)
    else:
        print(-1) 
if __name__ == '__main__':
    main()