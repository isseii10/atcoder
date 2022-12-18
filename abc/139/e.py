from collections import deque
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    match_id = [[-1]*n for _ in range(n)]
    id_num = 0
    for i in range(n):
        for j in range(n-1):
            one = i
            other = a[i][j]-1
            if match_id[one][other] == -1:
                match_id[one][other] = id_num
                match_id[other][one] = id_num
                id_num += 1

    #for i in range(n):
    #    print(match_id[i])

    edges = [[]*id_num for _ in range(id_num)]
    r_edges = [[]*id_num for _ in range(id_num)]

    for i in range(n):
        for j in range(n-2):
            one = i
            first = a[i][j] - 1
            second = a[i][j+1] - 1
            edges[match_id[one][first]].append(match_id[one][second])
            r_edges[match_id[one][second]].append(match_id[one][first])
    
    #for i in range(id_num):
    #    print(edges[i])    
    #print("================================")
    #for i in range(id_num):
    #    print(r_edges[i])

    day_1 = [] 
    for id in range(id_num):
        if len(r_edges[id]) == 0:
            day_1.append(id)
    
    seen = [0]*id_num

    def dfs(now):
        if seen[now] == 2:return INF
        if len(edges[now]) == 0:
            return 1 #葉だったら１を返す
        for nxt in edges[now]:
            seen[nxt] += 1
            if seen[nxt] == 1:
                dp[now] = max(dp[now], dfs(nxt) + 1)
            elif seen[nxt] == 2:
                return INF
            seen[nxt] = 0
        
        return dp[now]
        

    ans = INF
    for id in day_1:
        dp = [-1]*id_num # dp[i]は、match_idがiの試合から始めて大会が終了する日数
        ans = min(ans, dfs(id))
    
    if ans >= INF:
        print(-1)
    else:
        print(ans)
if __name__ == '__main__':
    main()