import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    s = input()[:-1]
    res = "b"
    count = 0
    while len(res) < n:
        count += 1
        if count % 3 == 1:
            res = 'a' + res + 'c'
        elif count % 3 == 2:
            res = 'c' + res + 'a'
        else:
            res = 'b' + res + 'b'
    if len(res) != n or res != s:
        print(-1)
    else:
        print(count)


if __name__ == '__main__':
    main()