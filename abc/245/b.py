import inspect
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
   n = int(input())
   a = set(map(int, input().split()))
   for i in range(2001):
        if i in a:
            continue
        print(i)
        exit()

if __name__ == '__main__':
    main()