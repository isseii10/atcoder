import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    h, w = map(int, input().split())
    s = [input()[:-1] for _ in range(h)]
    ans = 0
    for i in range(h-1):
        for j in range(w-1):
            ul = 1 if s[i][j] == '#' else 0
            ur = 1 if s[i][j+1] == '#' else 0
            dl = 1 if s[i+1][j] == '#' else 0
            dr = 1 if s[i+1][j+1] == '#' else 0

            if ul + ur + dl + dr == 1:
                ans += 1
            if ul + ur + dl + dr == 3:
                ans += 1
            
    print(ans)

if __name__ == '__main__':
    main()