import sys
from collections import Counter
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = [0]*n
    for i in range(n):
        mod[i] = a[i]%200
    
    c = Counter(mod)
    ans = 0
    for k, v in c.items():
        ans += v * (v-1) // 2
    
    print(ans)
    
if __name__ == '__main__':
    main()