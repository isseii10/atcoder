import sys

input = sys.stdin.readline
#sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353

def main():
    #grundy数の実験から
    n = int(input())
    now = 1
    x = 1
    flag = "A"
    while now < n:
        x *= 4
        now += x
        if now >= n:
            flag = "T"
            break
        now += x
        if now >= n:
            flag = "A"
            break
    if flag == "T":
        print("Takahashi")
    else:
        print("Aoki")
if __name__ == '__main__':
    main()