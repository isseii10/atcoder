import sys

input = sys.stdin.readline
#sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353

def main():
    n = int(input())
    A = list(map(int, input().split()))
    from collections import defaultdict
    d = defaultdict(int)
    over_red = 0
    for a in A:
        if a >= 3200:
            over_red += 1
            continue
        d[a//400] = 1

    print(max(sum(d.values()), 1), sum(d.values())+over_red)
    
if __name__ == '__main__':
    main()