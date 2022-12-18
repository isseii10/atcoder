import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, k = map(int, input().split())
    under = k-1
    upper = n-k
    all = n**3
    ans = under*upper * 6

    # underがkの時
    ans += upper * 3
    #upperがkの時
    ans += under * 3
    #underもupperもkの時
    ans += 1
    print(ans/all)
if __name__ == '__main__':
    main()