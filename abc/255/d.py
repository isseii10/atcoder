import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    min_a = a[0]
    max_a = a[-1]
    sa = [0] * (n+1)
    for i in range(n):
        sa[i+1] = sa[i] + a[i]
    
        
    for _ in range(q):
        x = int(input())
        if x <= min_a:
            ans =  sa[n] - n*abs(x)
        elif x >= max_a:
            ans = n*abs(x) - sa[n]
        else:
            idx = bisect_left(a, x)
            ans = (2*idx-n)*x + (sa[n] - 2*sa[idx])
        print(ans)



if __name__ == '__main__':
    main()