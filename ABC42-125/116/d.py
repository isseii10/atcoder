import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1 << 60
MOD = 10**9+7
#MOD = 998244353


def main():
    n, k = map(int, input().split())
    sushi = [[] for _ in range(n)]
    for _ in range(n):
        t, d = map(int, input().split())
        t -= 1
        sushi[t].append(d)

    for neta in sushi:
        neta.sort(reverse=True)
        if len(neta) == 0: #番兵
            neta.append(-INF)
    
    sushi.sort(reverse=True)
    #print(sushi)

    #sushi = [neta]*nになっている

    import heapq
    hq = []
    oisisa = 0
    #k個食べるので、食べられるネタの種類は最大k個
    for i in range(k):
        #k種類のnetaの中で一番美味しいやつを確保
        oisisa += sushi[i][0]
        for j in range(1, len(sushi[i])):
            #２番目以降の美味しさのやつはhqへ
            heapq.heappush(hq, -sushi[i][j])
    
    for i in range(k, n):
        #k種類以降のnetaについて、全部hpへ
        for j in range(len(sushi[i])):
            heapq.heappush(hq, -sushi[i][j])
    
    #k種類から減らしていく方向で更新
    res = oisisa + k**2
    for i in range(1, k)[::-1]:
        v = sushi[i][0] #減らす種類のやつ
        w = -heapq.heappop(hq) #食べてないやつの中で一番美味しいやつ
        if v < w:
            heapq.heappush(hq, -v)
            oisisa += w - v
        else:
            heapq.heappush(hq, -w)
        res = max(res, oisisa + i**2)
    
    print(res)



if __name__ == '__main__':
    main()