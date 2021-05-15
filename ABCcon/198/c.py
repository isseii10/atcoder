import decimal
import sys
import math, cmath
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    R, X, Y = map(int, input().split())
    dist = X**2 + Y ** 2
    if R**2 >= X**2 + Y**2:
        if R**2 == X**2 + Y**2:
            print(1)
        else:
            print(2)
        exit()
        
    flag = 1
    if (X**2 + Y**2) % R**2 == 0:
        flag = 0
    #print(dist)
    #print(abs(complex(100000, 100000)))
    ok = 0
    ng = 2000000
    while ng - ok > 1:
        mid = (ok+ng) // 2
        if (mid * R)**2 > dist:
            ng = mid
        else:
            ok = mid
    print(ok + flag)


if __name__ == '__main__':
    main()