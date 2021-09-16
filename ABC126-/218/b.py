import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    p = list(map(int, input().split()))
    alpha = "abcdefghijklmnopqrstuvwxyz"
    #print(len(alpha))
    s = ""
    for pi in p:
        s += alpha[pi-1]
    print(s)
if __name__ == '__main__':
    main()