#from sys import setrecursionlimit
#setrecursionlimit(10**7)
from sys import stdin
input = stdin.readline
INF = float('inf')

def main():
    n, k = map(int, input().split())
    ans = k
    for _ in range(n-1):
        ans *= k-1
    print(ans)
if __name__ == '__main__':
    main()