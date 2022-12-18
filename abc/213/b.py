import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i, score in enumerate(a):
        b.append((score, i))
    b.sort()
    print(b[-2][1]+1)
    
if __name__ == '__main__':
    main()