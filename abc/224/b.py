import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]

    ok = True
    for i1 in range(h):
        for j1 in range(w):
            for i2 in range(h):
                for j2 in range(w):
                    if i1 >= i2 or j1 >= j2:continue
                    if a[i1][j1] + a[i2][j2] > a[i2][j1] + a[i1][j2]:
                        ok = False
                        break
    
    if ok:
        print("Yes")
    else:
        print("No")
if __name__ == '__main__':
    main()