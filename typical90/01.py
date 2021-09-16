import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, l = map(int, input().split())
    k = int(input())
    a = list(map(int, input().split()))
    a.append(l)
    #print(a)

    ok = 0
    ng = 10**9
    
    num = n - k
    # もっとも短いピースをx以上にできるか？
    def check(x):
        # つまり、全てのピースをx以上にできるか？
        # (こういう言い換えが苦手)
        count = 0
        prev = 0
        for i in range(n+1):
            if a[i] - prev >= x:
                prev = a[i]
                count += 1
        if count >= k+1:
            return True
        else:
            return False


    while ng - ok > 1:
        mid = (ok+ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    print(ok)
if __name__ == '__main__':
    main()