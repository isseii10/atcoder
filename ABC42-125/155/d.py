import sys
from bisect import bisect_right, bisect_left
from math import floor

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353

def check(x, k, A):
    #積がx以下になるものを数える
    # O(nlogn)
    count = 0
    if x < 0:
        #正＊負
        for i, a in enumerate(A):
            if a == 0:continue
            res = 0
            target = x / a
            if a > 0:
                #負の中から探す
                j = bisect_right(A, target)
                res += j
            else:
                #正の中から探す
                j = bisect_left(A, target)
                res += len(A) - j
            if a*a <= x:
                res -= 1
            count += res
        count //= 2 # 重複消す

    elif x > 0:
        #正正　か　負負
        for i, a in enumerate(A):
            res = 0
            if a == 0:
                res += len(A)
            else:
                target = x / a
                if a > 0:
                    #正に制限がある    
                    j = bisect_right(A, target)
                    res += j
                else:
                    #負に制限がある
                    j = bisect_left(A, target)
                    res += len(A) - j
        
            if a * a <= x:
                res -= 1
            count += res
        count //= 2

    else:
        for a in A:
            res = 0
            if a == 0:
                res += len(A)
            else:
                if a > 0:
                    #負(0含む)から
                    zero = bisect_right(A, 0)
                    res += zero
                else:
                    #正（０含む）
                    zero = bisect_left(A, 0)
                    res += len(A) - zero
            
            if a*a <= x:
                res -= 1
            count += res
        count //= 2

    if count < k:
        return True
    else:
        return False 



def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    left = -10**18
    right = 10 ** 18 + 1
    while right - left > 1:
        mid = (right+left)//2
        #積がmid以下になる組み合わせの数がk個より少ないか？
        #Yes left = mid
        #No right = mid
        if check(mid, k, A):
            left = mid
        else:
            right = mid
    
    print(right)

    
if __name__ == '__main__':
    main()