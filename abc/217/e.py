import sys
import heapq
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    q = int(input())
    a = deque() #sortされていない配列
    a_hq = [] #sort済み配列
    for _ in range(q):
        query = list(map(int, input().split()))
        #print(query)
        if query[0] == 1:
            x = query[1]
            a.append(x)
        elif query[0] == 2:
            # a_hqが空でない時はquery3が以前に行われているので、a_hqからpop
            if a_hq:
                print(heapq.heappop(a_hq))
            # a_hqが空の時はquery1で追加した順に出てくるので、aからpop
            else:
                print(a.popleft())
        else:
            # query3では全部sortされるので、aの要素を全てa_hqに移す
            while a:
                heapq.heappush(a_hq, a.popleft())
    
    
    
if __name__ == '__main__':
    main()