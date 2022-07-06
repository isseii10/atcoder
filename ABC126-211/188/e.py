import sys
sys.setrecursionlimit(10000000)
n, m = map(int, input().split())
a = list(map(int, input().split()))
edges = [[]*n for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    edges[x].append(y)

#自分より、子であるノードの最大値が前計算で分かれば、O(n)で解ける
#　-> dfs帰りがけ順で最大値を求めていく

#max_a[i] := i番目のノードの子の最大値（i番目のノードは含まない） 
max_a = [-1]*n
visited = [False]*n

def dfs(pp, p):
    visited[p] = True
    #葉だったり、非連結の単一のノードだった場合は何もしない
    if not edges[p]:return
    #子が存在する場合は探索していく
    for c in edges[p]:
        if c == pp:continue
        dfs(p, c)
        max_a[p] = max(max(max_a[p], a[c]), max_a[c])


for i in range(n):
    if visited[i]:continue
    dfs(-1, i)

#print("max_a is :{}".format(max_a))
#print('visited is :{}'.format(visited))
ans = -float('INF')
for i in range(n):
    if max_a[i] == -1:continue
    ans = max(ans, max_a[i]-a[i])
print(ans)