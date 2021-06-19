import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    left = 0
    right = 10**9
    while right - left > 1:
        mid = (left+right) // 2
        money = mid*(mid+1) // 2
        if money < n:
            left = mid
        else:
            right = mid
    print(right)
if __name__ == '__main__':
    main()