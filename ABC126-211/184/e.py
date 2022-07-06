#from sys import setrecursionlimit
#setrecursionlimit(10**7)
from sys import stdin
input = stdin.readline
INF = float('inf')

from collections import deque

def main():
    h, w = map(int, input().split())
    a = [input()[:-1] for _ in range(h)]
    cost = [[INF]*w for _ in range(h)]
    start = [0, 0]
    goal = [0, 0]
    alpha = [[] for _ in range(26)]
    for i in range(h):
        for j in range(w):
            if a[i][j] == 'S':
                start[0] = i
                start[1] = j
            elif a[i][j] == 'G':
                goal[0] = i
                goal[1] = j
            elif a[i][j] == '.' or a[i][j] == '#':
                continue
            else:
                alpha[ord(a[i][j])-ord('a')].append((i, j))
            
    #print(alpha)
    q = deque([start])
    cost[start[0]][start[1]] = 0
    cost_tele = [INF]*26
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    while q:
        y, x = q.popleft()
        # y=-1の時,テレポートしてきた。xはa~z(のord)
        if y == -1:
            # xというテレポーターがある位置x２、y２を全てみる
            for y2, x2 in alpha[x]:
                # コストに変更があるなら（このテレポートの方が早く着くなら）
                # コストを更新して、appendleft
                if cost[y2][x2] > cost_tele[x]+1:
                    cost[y2][x2] = cost_tele[x]+1
                    q.appendleft([y2, x2])
            continue
        #y != -1の時は通常移動をみる
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0 <= ny < h and 0 <= nx < w:
                if a[ny][nx] == '#':
                    continue
                if cost[ny][nx] > cost[y][x] + 1:
                    cost[ny][nx] = cost[y][x] + 1
                    q.append([ny, nx])
                if ord('a') <= ord(a[ny][nx]) <= ord('z'):
                    tele = ord(a[ny][nx]) - ord('a')
                    if cost_tele[tele] > cost[y][x] + 1:
                        cost_tele[tele] = cost[y][x] + 1
                        q.append([-1, tele])
        
        
    #for i in range(h):
    #    print(cost[i])
    #print(cost_tele)
    ans = cost[goal[0]][goal[1]]
    if ans == INF:
        print(-1)
    else:
        print(ans)




        



if __name__ == '__main__':
    main()