import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    ans = 0
    count = 1
    for i in range(n-1):
        if a[i] == a[i+1]:
            count += 1
            continue
        if k >= (a[i] - a[i+1])*count:
            ans += (a[i+1]+1 + a[i])*(a[i]-a[i+1]) // 2 * count
            k -= (a[i]-a[i+1])*count
            count += 1
        else:
            #この分岐に入ったら必ず終了なので最後にbreak
            tmp_k = k // count
            ans += (2*a[i] - (tmp_k-1)) * tmp_k // 2 * count
            a[i] = a[i] - tmp_k
            tmp_k = k % count
            ans += tmp_k * a[i]
            break
        

    else:
        #終了の分岐に入らずに最後まできたので最後の計算
        if k >= a[-1]*n:
            ans += (1+a[-1])*a[n-1] // 2 * n
        else:
            tmp_k = k // n
            ans += (2*a[-1] - (tmp_k-1))*tmp_k // 2 * n
            a[-1] = a[-1] - tmp_k
            tmp_k = k % n
            ans += tmp_k * a[-1]
    
    print(ans)






if __name__ == '__main__':
    main()