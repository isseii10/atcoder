import sys

input = sys.stdin.readline
#sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a[-1]-a[0])
    
if __name__ == '__main__':
    main()