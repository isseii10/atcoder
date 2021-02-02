import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    bit = [0]*40
    for a in A:
        loop_count = 0
        _a = a
        while _a > 0:
            if _a % 2:
                bit[loop_count] += 1
            _a //= 2
            loop_count += 1

    dp = [[-1]*2 for _ in range(41)]
    dp[40][0] = 0
    #dp[i][smallflag] 下からi桁目まで見た時のfの最大値
    # smallflag = 1 ->True (ちっちゃい)
    # smallflag = 0 ->False(上からi桁目までは一緒)

    # dpの[i]を下からi桁にしたので逆順に回すことで上から見ていける
    for i in range(40)[::-1]:
        one = bit[i]
        zero = n - one

        if dp[i+1][1] >= 0:
            #ちっちゃいやつからちっちゃいやつへの遷移
            #もうすでにちっちゃいので、下位桁はなにであってもちっちゃいの確定
            dp[i][1] = max(dp[i][1], dp[i+1][1] + (1<<i)*max(one, zero))
        if dp[i+1][0] >= 0:
            if k >> i & 1:
                #一緒のやつからちっちゃくなる遷移
                #iでビットが立っていたら、そこを０にすることでちっちゃくなれる
                #iでビットが立っていなかったらちっちゃいのに遷移はできない
                dp[i][1] = max(dp[i][1], dp[i+1][0] + (1<<i)*one)
                #一緒のやつから一緒のやつへの遷移
                dp[i][0] = max(dp[i][0], dp[i+1][0] + (1<<i)*zero)
            else:
                #一緒のやつから一緒のやつへの遷移
                dp[i][0] = max(dp[i][0], dp[i+1][0] + (1<<i)*one)

        
    print(dp[0][1], dp[0][0])


        
    
if __name__ == '__main__':
    main()