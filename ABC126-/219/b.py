import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    s1 = input()[:-1]
    s2 = input()[:-1]
    s3 = input()[:-1]
    t = input()[:-1]
    ans = ""
    for c in t:
        if c == '1':
            ans += s1
        if c == '2':
            ans += s2
        if c == '3':
            ans += s3
    print(ans)
if __name__ == '__main__':
    main()