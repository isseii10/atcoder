import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353

def bisect_de(sa, de_mean, i, n):
    left = i
    right = n
    while right - left > 1:
        mid = (left+right)//2
        if sa[mid] - sa[i] <= de_mean:
            left = mid
        else:
            right = mid
    return left



def main():
    from bisect import bisect_left, bisect_right
    n = int(input())
    a = list(map(int, input().split()))
    sa = [0]*(n+1)
    for i in range(n):
        sa[i+1] += sa[i] + a[i]
    
    #bc, deに分ける境界を全探索
    ans = INF
    for i in range(2, n-1):
        bc_mean = (sa[i]+1)//2
        de_mean = (sa[n]-sa[i]+1)//2
        print(sa)
        print("i = {}".format(i))
        print("bc_mean = {}".format(bc_mean))
        print("de_mean = {}".format(de_mean))
        idx_bc = bisect_left(sa, bc_mean, 1, i)
        idx_de = bisect_de(sa, de_mean, i+1, n)
        p, q, r, s = sa[idx_bc], sa[i]-sa[idx_bc], sa[idx_de]-sa[i], sa[n]-sa[idx_de]
        ans = min(ans, abs(max(p, q, r, s)-min(p, q, r, s)))
        print(p, q, r, s)
        print("--------------------------------------")
    print(ans)

if __name__ == '__main__':
    main()