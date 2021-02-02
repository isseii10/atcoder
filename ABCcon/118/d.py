import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, m = map(int, input().split())
    cost = [0, 2, 5, 5, 4, 5, 6 ,3, 7, 6]
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    #print(A)

    dp = [-INF]*(n+1)
    #dp[i] := ちょうどi本使うときの最大桁数
    dp[0] = 0
    for i in range(1, n+1):
        for j in range(m):
            if i-cost[A[j]] < 0:continue
            dp[i] = max(dp[i], dp[i-cost[A[j]]] + 1)
    #print(dp)
    digit = dp[n]
    ans = [0]*digit
    n_ = n
    for i in range(digit):
        for a in A:
            if n_ - cost[a]<0:continue
            if dp[n_-cost[a]] == dp[n_] - 1:
                ans[i] = str(a)
                n_ -= cost[a]
                break
    print("".join(ans))

    
    

if __name__ == '__main__':
    main()