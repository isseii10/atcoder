n, m = map(int, input().split())
a = list(map(int, input().split()))
edges = [[]*n for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    edges[x].append(y)

#自分より、親側であるノードの最小値が前計算で分かれば、O(n)で解ける
#　-> dfs行きがけ順(ぽい感じ)で最小値を求めていく
#  x < y という制約から、DAGなので、頂点idxの小さい順から見ていけば良い（DAG上のDP）

#min_a[i] := i番目のノードのより親側の最小値（i番目のノードは含まない） 
min_a = [float('inf')]*n

for p in range(n):
    for c in edges[p]:
        min_a[c] = min(min(min_a[c], min_a[p]), a[p])

#print(min_a)

ans = -float('inf')
for i in range(n):
    if min_a[i]==float('inf'):continue
    ans = max(ans, a[i]-min_a[i])
print(ans)
