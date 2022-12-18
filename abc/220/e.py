import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
#MOD = 10**9+7
MOD = 998244353


def main():
    n, d = map(int, input().split())

    dp = [0]*n
    #dp[i]は、葉まで深さnの木の距離がdの個数

    ans = 0
    for i in range(n):
        depth_now = i
        depth_to = n-1-i #葉までの深さ
        #その深さの頂点すう　ここで折る
        m = 2**depth_now
        if d > depth_to * 2:continue
        #left = 0の時
        if d <= depth_to:
            ans += m*2*2**d
        left = 1
        while left <= depth_to:
            if left == d:break
            ans += m*(2**(left-1) * 2**(d - left-1) * 2)
            print(i, m*(2**(left-1) * 2**(d - left-1))*2)
            ans %= MOD
            left += 1
    print(ans)
        

if __name__ == '__main__':
    main()