import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def divide_count(num, n):
    count = 0
    while num % n == 0:
        num //= n
        count += 1
    return count

def main():
    n, d = map(int, input().split())

    #サイコロは2, 3, 5の素数が出る
    count_2 = divide_count(d, 2)
    count_3 = divide_count(d, 3)
    count_5 = divide_count(d, 5)

    # dが2, 3, 5以外の素因数を持つとダメ
    if d != 2**count_2 * 3**count_3 * 5**count_5:
        print(0)
        exit()

    dp = [[[[0]*(count_5+1) for _ in range(count_3+1)] for _ in range(count_2+1)] for _ in range(n+1)]

    dp[0][0][0][0] = 1

    for i in range(n):
        for c2 in range(count_2+1):
            for c3 in range(count_3+1):
                for c5 in range(count_5+1):
                    tmp = dp[i][c2][c3][c5]
                    if tmp == 0: continue
                    #1
                    dp[i+1][c2][c3][c5] += tmp
                    #2
                    dp[i+1][min(count_2, c2+1)][c3][c5] += tmp
                    #3
                    dp[i+1][c2][min(count_3, c3+1)][c5] += tmp
                    #4
                    dp[i+1][min(count_2, c2+2)][c3][c5] += tmp
                    #5
                    dp[i+1][c2][c3][min(count_5, c5+1)] += tmp
                    #6
                    dp[i+1][min(count_2, c2+1)][min(count_3, c3+1)][c5] += tmp
    
    print(dp[n][count_2][count_3][count_5] / (6**n))


if __name__ == '__main__':
    main()