import sys
from collections import defaultdict

input = sys.stdin.readline
#sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353

def bit_tansaku(n, abc, ma, mb):
    res = defaultdict(list)
    for i in range(1<<n):
        a = 0
        b = 0
        c = 0
        for j in range(n):
            if i >> j & 1:
                aj, bj, cj = abc[j]
                a += aj
                b += bj
                c += cj
        res[a*mb - b*ma].append(c)
    return res



def main():
    n, ma, mb = map(int, input().split())
    abc = [list(map(int, input().split())) for _ in range(n)]
    abc1, abc2 = abc[:n//2], abc[n//2:]
    d1 = bit_tansaku(len(abc1), abc1, ma, mb)
    d2 = bit_tansaku(len(abc2), abc2, ma, mb)
    for v in d2.values():
        v.sort()

    ans = INF
    for ab1, c1_list in d1.items():
        ab2 = -ab1
        for c1 in c1_list: 
            res = c1
            if ab2 not in d2.keys():continue
            c2_list = d2[ab2]
            res += c2_list[0]
            if res == 0:
                if len(c2_list) == 1:continue
                res += c2_list[1]
            ans = min(ans, res)
    
    if ans == INF:
        ans = -1
    
    print(ans)



    
    

if __name__ == '__main__':
    main()