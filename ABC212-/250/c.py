import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, q = map(int, input().split())
    now = [i for i in range(n)]
    position = [i for i in range(n)]
    
    for _ in range(q):
        x = int(input())
        x -= 1
        idx = position[x]
        if idx == n-1:
            swap_idx = idx - 1
        else:
            swap_idx = idx + 1
        a = now[idx]
        b = now[swap_idx]
        position[a] = swap_idx
        position[b] = idx
        now[idx], now[swap_idx] = now[swap_idx], now[idx]
        
    for i in range(n):
        now[i] += 1
    
    print(*now)

        
if __name__ == '__main__':
    main()