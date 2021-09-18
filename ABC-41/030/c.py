import sys
from bisect import bisect_left
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, m = map(int, input().split())
    x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    to_b_idx = 0
    to_a_idx = 0
    now = 0 #now%2=0 : Aにいる　now%2=1 Bにいる
    now_time = 0
    while to_b_idx < n and to_a_idx < m:
        if now % 2 == 0:
            to_b_idx = bisect_left(a, now_time)
            if to_b_idx == n:
                break
            now_time = a[to_b_idx] + x
            now += 1
        else:
            to_a_idx = bisect_left(b, now_time)
            if to_a_idx == m:
                break
            now_time = b[to_a_idx] + y
            now += 1
    print(now // 2)
    
if __name__ == '__main__':
    main()