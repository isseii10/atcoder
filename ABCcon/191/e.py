import heapq
hq = []

def prt_hq():
    for i in hq:
        print(-i)
    print('\n')

a = [8, 5, 7, 3, 10, 9, 6, 1, 20]
for i in a:
    heapq.heappush(hq, -i)
    prt_hq()

