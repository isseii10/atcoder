import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    q = int(input())
    d = deque([])
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            x, c = query[1:]
            d.append((x, c))
        else:
            c = query[1]
            ans = 0
            while c > 0:
                number, count = d.popleft()
                if count > c:
                    d.appendleft((number, count-c))
                    ans += number * c
                    c = 0
                else:
                    ans += number * count
                    c -= count
            print(ans)



if __name__ == '__main__':
    main()