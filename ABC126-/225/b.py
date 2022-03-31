import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    G = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)
    
    for i in range(n):
        if len(G[i]) != 1 and len(G[i]) != n-1:
            print("No")
            break
    else:
        print("Yes")

if __name__ == '__main__':
    main()