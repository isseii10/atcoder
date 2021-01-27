from collections import defaultdict
#defaultdictは順序保証されていない
n, C = map(int, input().split())
d = defaultdict(int)
for _ in range(n):
    a, b, c = map(int, input().split())
    a -= 1
    d[a] += c
    d[b] -= c
#defaultdictやdictはソートできないので、sortedでタプル（key, value）のリストを返す
#ということは別に最初からソートできるリスト構造でよかったてなった
sort_d = sorted(d.items())
#print(sort_d)
pre_date = -1
now_cost = 0
all_cost = 0
for date, cost in sort_d:
    #print("date:{}, cost:{}".format(date, cost))
    if pre_date != -1:
        all_cost += min(C, now_cost) * (date-pre_date)
    now_cost += cost
    pre_date = date
print(all_cost)
