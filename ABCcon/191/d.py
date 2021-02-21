import sys
from math import floor
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353

def isInside(circle, x):


def count_upper(circle, ok):
    X, Y, R = circle
    ok = floor(Y)
    if not isInside(circle, ok):continue
    ng = ok + floor(R) + 10

def count_lower(circle, ok):
    X, Y, R = circle
    ok = floor(Y)



def main():
    circle = tuple(map(float, input().split()))
    X, Y, R = circle
    ans = 0
    for x in range(floor(X) - (floor(R)+10), floor(X) + (floor(R)+10)):
        ans += count_lower(circle, x)
        ans += count_upper(circle, x)
    print(ans)

if __name__ == '__main__':
    main()