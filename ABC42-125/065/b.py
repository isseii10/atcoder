import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    from collections import deque
    q = deque([0])
    pushed = [-1]*n
    pushed[0] = 0
    while q:
        p = q.popleft()
        c = a[p]-1
        if pushed[c] != -1:
            continue
        pushed[c] = pushed[p]+1
        q.append(c)
    
    print(pushed[1])


if __name__ == '__main__':
    main()