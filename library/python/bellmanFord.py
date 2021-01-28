INF = float('inf')

#ノーマルなベルマンフォード
def BellmanFord(n, edges, cost, s) -> bool:
    """
    edgesは辺のリスト(隣接リストではない)
    負の閉路が検出されたらfalseを返す
    """
    cost[s] = 0
    for i in range(n):
        for fr, to, c in edges:
            if cost[to] > cost[fr] + c:
                cost[to] = cost[fr] + c
                if i == n-1:
                    return False
    
    return True


# 始点から終点へのパス上での閉路の検出
def bellmanFord(n, edges, cost, s, g) -> bool:
    """
    始点sから到達可能かつ終点gへ到達可能は負閉路が検出されたときFalse
    それ以外True

    costはINFに初期化されたリストを渡す
    """
    cost[s] == 0
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
