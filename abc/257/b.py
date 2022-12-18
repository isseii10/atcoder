import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, k, q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    field = [0]*(n+1)
    for i, a in enumerate(A):
        field[a] = 1
    
    for i in range(q):
        li = L[i]
        idx = -1
        for j in range(1, n+1):
            if field[j]:li -= 1
            if li == 0:
                idx = j
                break
        if idx == n:continue
        if field[idx+1]:continue
        field[idx] = 0
        field[idx+1] = 1
    
    ans = []
    for i in range(1, n+1):
        if field[i]:
            ans.append(i)
    print(*ans)

        
if __name__ == '__main__':
    main()