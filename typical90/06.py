import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, K = map(int, input().split())
    s = input()[:-1]    
    nxt = [[-1]*26 for _ in range(n)]
    #nxt[i][c]は、i文字目以降でcが初めて現れるidx
    
    for i in range(26):
        for j in range(n):
            if ord(s[n-j-1]) - ord("a") == i:
                nxt[n-j-1][i] = n-j-1
            else:
                if j == 0:continue
                nxt[n-j-1][i] = nxt[n-j][i]
    
    print(nxt)

    
if __name__ == '__main__':
    main()