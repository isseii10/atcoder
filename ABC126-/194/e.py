import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    mex = 0
    seen = [0] * (n+1)
    for i in range(m):
        seen[A[i]] += 1 
        while seen[mex] != 0:
            mex += 1
    #print(mex)
    min_mex = mex
    #print(min_mex)
    for l in range(1, n-m+1):
        left = A[l-1]
        right = A[l+m-1]
        if left == right:continue

        seen[left] -= 1
        if left < mex:
            mex = left
        seen[right] += 1
        while seen[mex] != 0:
            mex += 1
        #print(mex)
        
        min_mex = min(min_mex, mex)
    print(min_mex)
    #print(min_mex)

    
if __name__ == '__main__':
    main()