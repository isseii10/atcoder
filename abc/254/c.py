import sys
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    sorted_a = sorted(a)
    mod_k = [[] for _ in range(k)]
    for i, num in enumerate(a):
        heapq.heappush(mod_k[i%k], num)
    for i in range(n):
        if sorted_a[i] == mod_k[i%k][0]:
            heapq.heappop(mod_k[i%k])
        else:
            print("No")
            exit()
    print("Yes")
        
if __name__ == '__main__':
    main()