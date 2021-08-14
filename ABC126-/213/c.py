import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    h, w, n = map(int, input().split())
    card_y = []
    card_x = []
    card = []
    used_y = set()
    used_x = set()
    for _ in range(n):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        card.append((a, b))
        if a not in used_y: 
            card_y.append(a)
            used_y.add(a)
        if b not in used_x: 
            card_x.append(b)
            used_x.add(b)
    
    card_x.sort()
    card_y.sort()

    for a, b in card:
        print(bisect_left(card_y, a)+1, bisect_left(card_x, b)+1)


    
if __name__ == '__main__':
    main()