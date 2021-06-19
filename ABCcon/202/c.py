import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    Bc = [0]*n
    for i in range(n):
        idx = C[i] - 1
        Bc[i] = B[idx]
    
    Bc_count = defaultdict(int)
    for i in range(n):
        Bc_count[Bc[i]] += 1

    ans = 0
    for i in range(n):
        a = A[i]
        ans += Bc_count[a]
        
    
    print(ans)

if __name__ == '__main__':
    main()