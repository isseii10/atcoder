#from sys import setrecursionlimit
#setrecursionlimit(10**7)
from sys import stdin
input = stdin.readline
from collections import defaultdict
INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    h, w, n = map(int, input().split())
    ab = list(tuple(map(int, input().split())) for _ in range(n))
    rec_ul = defaultdict(int)
    for a, b in ab:
        for i in range(-2, 1):
            for j in range(-2, 1):
                ul_h = a+i
                ul_w = b+j
                #print("a, b = {}, {}".format(a, b))
                #print("ul_h, ul_w = {}, {}".format(ul_h, ul_w))
                if ul_h > 0 and ul_w > 0 and ul_h+2 <= h and ul_w+2 <= w:
                    rec_ul[(ul_h, ul_w)] += 1
    
    #print(rec_ul)

    ans = [0]*10
    for v in rec_ul.values():
        ans[v] += 1

    ans[0] = (h-2)*(w-2) - sum(ans)
    for i in range(10):
        print(ans[i])

if __name__ == '__main__':
    main()