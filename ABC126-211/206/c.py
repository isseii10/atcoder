import sys
from collections import Counter

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    all = n * (n-1) // 2
    for num, count in c.items():
        if count == 1:continue
        all -= count * (count -1) // 2
    print(all)
if __name__ == '__main__':
    main()