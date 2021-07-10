import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    p = int(input())
    coin_price = 1*2*3*4*5*6*7*8*9*10
    ans = 0
    ten = 10
    while p > 0:
        coin_num = p // coin_price
        p -= coin_num*coin_price
        coin_price = coin_price // ten
        ten -= 1
        ans += coin_num
    print(ans)

if __name__ == '__main__':
    main()