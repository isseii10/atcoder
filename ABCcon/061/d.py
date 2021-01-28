import sys

input = sys.stdin.readline
#sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353

# 始点から終点へのパス上での閉路の検出
def bellmanFord(n, edges, cost, s, g) -> bool:
    """
    始点sから到達可能かつ終点gへ到達可能は負閉路が検出されたときFalse
    それ以外True

    costはINFに初期化されたリストを渡す
    """
    cost[s] = 0
    for i in range(2*n):
        for fr, to, c in edges:
            if cost[fr] < INF and cost[fr] + c < cost[to]:
                if i >= n-1 and to == g:
                    return False
                elif i >= n-1:
                    cost[to] = -INF
                else:
                    cost[to] = cost[fr] + c
    return True




def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((a-1, b-1, -c))

    cost = [INF]*n
    if bellmanFord(n, edges, cost, 0, n-1):
        print(-cost[n-1])
    else:
        print("inf")
    
    
    

    
if __name__ == '__main__':
    main()