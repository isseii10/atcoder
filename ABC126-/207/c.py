import sys
from collections import OrderedDict
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    kukan_list = []
    for _ in range(n):
        t, l, r = map(int, input().split())
        l *= 2
        r *= 2
        l -= 1
        r -= 1
        if t == 1:
            pass
        elif t == 2:
            r -= 1
        elif t == 3:
            l += 1
        else:
            l += 1
            r -= 1

        kukan_list.append((l, r))
    
    ans = 0
    #print(kukan_list)
    for i in range(n-1):
        l1, r1 = kukan_list[i]
        for j in range(i+1, n):
            l2, r2 = kukan_list[j]

            if r1 < l2 or r2 < l1:
                continue
            ans += 1
    print(ans)


        
if __name__ == '__main__':
    main()