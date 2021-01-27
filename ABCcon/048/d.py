import sys

input = sys.stdin.readline
#sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353

def main():
    s = input()[:-1]
    n = len(s)
    iseven = (n+1) % 2
    isequal = 0
    if s[0] == s[-1]:
        isequal = 1
    if iseven^isequal:
        print("Second")
    else:
        print("First")

if __name__ == '__main__':
    main()