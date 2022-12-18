import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    s = input()[:-1]
    n = int(input())
    for _ in range(n):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        #print(s[:l])
        #print(s[l:r+1][::-1])
        #print(s[r+1:])
        s = s[:l] + s[l:r+1][::-1] + s[r+1:]
    print(s)
if __name__ == '__main__':
    main()