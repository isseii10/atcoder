import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
#MOD = 10**9+7
MOD = 998244353


def main():
    n, d = map(int, input().split())

    #前計算2**x
    kaijo = [1]*(2*n+1)
    for i in range(2*n):
        kaijo[i+1] = (kaijo[i]*2) % MOD

    ans = 0
    for now in range(n):
        #nowは今見ている頂点の深さ
        depth_now_to_leaf = n-1-now #今見ている頂点から葉までの深さ
        if d > depth_now_to_leaf * 2:continue

        #今見ている深さの頂点数m　
        m = kaijo[now]
        #今見ている頂点につながる葉の数l
        l = kaijo[depth_now_to_leaf]


        res = 0
        #場合分けしていく

        #その頂点から片方にパスが伸びる場合

        if d <= depth_now_to_leaf:
            #葉の数だけパスがあり,頂点交換してかける２
            res += l*2
            res %= MOD


        #その頂点から両側にパスが伸びる場合

        #一方にxだけ伸びているとすると、もう一方はd-xだけ伸びている
        # 2**(x-1) * 2**(d-x-1) = 2**(d-2)

        #片側の長さは1からd-1まで (d-1通り) のはずだが、
        # depth_now_to_leafとの大小関係を加味する必要がある
        # x <= depth_now_to_leaf かつ d-x <= depth_now_to_leafである場合の数は、
        # max(1, d-depth_now_to_leaf) <= x <= depth_now_to_leaf
        # depth_now_to_leaf - max(1, d-depth_now_to_leaf)+1(通り)
        res += (min(d-1, depth_now_to_leaf) - max(1, d-depth_now_to_leaf)+1) * kaijo[d-2] * 2
        res %= MOD


        #resは今見ている深さの一つの頂点についてなので、mかける
        res *= m
        res %= MOD

        ans = (ans + res) % MOD


    print(ans)
        

if __name__ == '__main__':
    main()