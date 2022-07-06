n = 6
edge = [[] for _ in range(n)]
for i in range(1, 5):
    edge[0].append((i, 100))
    edge[i].append((0, 100))
edge[0].append((5, 1))
edge[5].append((0, 1))

for i in range(1, 5):
    edge[5].append((i, 1))
    edge[i].append((5, 1))

print(edge)

from collections import deque
from heapq import heappush, heappop
INF = 1 << 60
dist_bfs = [INF]*n
dist_dji = [INF]*n
dist_bfs[0] = 0
dist_dji[0] = 0

q = deque()
q.append(0)
count_bfs = 0
while q:
    p = q.pop()
    for c, dd in edge[p]:
        if dist_bfs[c] <= dist_bfs[p] + dd:
            continue
        count_bfs += 1
        dist_bfs[c] = dist_bfs[p] + dd
        q.append(c)

hq = []
heappush(hq, (dist_dji[0], 0))
count_dji = 0
while hq:
    dist_p, p = heappop(hq)
    for c, dd in edge[p]:
        if dist_dji[c] <= dist_p + dd:continue
        count_dji += 1
        dist_dji[c] = dist_p + dd
        heappush(hq, (dist_dji[c], c))

print(dist_bfs, count_bfs)
print(dist_dji, count_dji)