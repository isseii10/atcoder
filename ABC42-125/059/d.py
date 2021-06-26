import sys

input = sys.stdin.readline
#sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353

def main():
    x, y = map(int, input().split())
    #実験より、abs(x-y) <= 1のとき負けることがわかった
    if abs(x-y) <= 1:
        print("Brown")
    else:
        print("Alice")
if __name__ == '__main__':
    main()