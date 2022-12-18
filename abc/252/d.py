import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    A = list(map(int, input().split()))
    total = (n)*(n-1)*(n-2) // 6
    d = defaultdict(int)
    for a in A:
        d[a] += 1
    # 全部同じ時
    res = 0
    for _, v in d.items():
        if v >= 3:
            res += v*(v-1)*(v-2) // 6
    
    # ふたつ同じで一つ異なるとき
    for _, v in d.items():
        if v >= 2:
            res += (v*(v-1) // 2)*(n-v)
    print(total - res)
    
            
            
    
if __name__ == '__main__':
    main()