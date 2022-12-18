import sys
from bisect import bisect_right

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    a1, a2 = a[:n//2], a[n//2:]

    n1 = len(a1)
    n2 = len(a2)

    def bit(n, a):
        res = []
        for i in range(1 << n):
            tmp = 0
            for j in range(n):
                if i >> j & 1:
                    tmp += a[j]
            res.append(tmp)
        return res
    
    res1 = bit(n1, a1)
    res2 = bit(n2, a2)
    res2.sort()
    ans = 0
    for time1 in res1:
        if time1 > t:continue
        time2 = t - time1
        idx = bisect_right(res2, time2)
        ans = max(ans, time1+res2[idx-1])
    print(ans)

    





if __name__ == '__main__':
    main()