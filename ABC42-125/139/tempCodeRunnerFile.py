import sys
import copy

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    A = [list(map(int, input().split())) for _ in range(n)]

    point = [0]*n
    day = 0
    finish_all = [False]*n
    yesterday = [True]*n

    while True:
        player = [False]*n
        played = set()
        for a in range(n):
            if not yesterday[a]:
                continue
            if player[a] or finish_all[a]:
                continue
            b = A[a][point[a]]
            b -= 1
            if player[b] or finish_all[b]:
                continue
            a_ = A[b][point[b]]
            a_ -= 1
            if a == a_:
                if a < b:
                    played.add((a, b))
                else:
                    played.add((b, a))
                player[a] = True
                point[a] += 1
                if point[a] == n-1:
                    finish_all[a] = True
                player[b] = True
                point[b] += 1
                if point[b] == n-1:
                    finish_all[b] = True

        if len(played)==0:
            print(-1)
            exit()

        day += 1
        if sum(point) == n*(n-1):
            break

        yesterday = copy.copy(player)


    print(day)

    
if __name__ == '__main__':
    main()