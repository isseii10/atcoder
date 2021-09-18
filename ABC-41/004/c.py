import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    x = n // 5
    start_idx = x % 6
    cards = ["1", "2", "3", "4", "5", "6"]
    cards = cards[start_idx:] + cards[:start_idx]
    y = n % 5

    for i in range(y):
        cards[i], cards[i+1] = cards[i+1], cards[i]
    print("".join(cards))


if __name__ == '__main__':
    main()