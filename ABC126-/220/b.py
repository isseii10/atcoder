import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    k = int(input())
    a, b = input().split()
    def to10(c):
        res = 0
        for i, ci in enumerate(c[::-1]):
            ci = int(ci)
            res += ci*k**i
        return res

    a_10 = to10(a) 
    b_10 = to10(b)
    print(a_10*b_10)
if __name__ == '__main__':
    main()