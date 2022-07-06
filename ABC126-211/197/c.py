import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    A = list(map(int, input().split()))
    if n == 1:
        print(A[0])
        exit()

    kukan = 1 << (n-1)
    
    ans = INF
    for i in range(kukan):
        res = 0
        or_res = A[n-1]
        for j in range(n-1):
            if i >> j &1:
                res = res ^ or_res
                or_res = A[n-(j+2)]
            else:
                #print(A[n-(j+2)])
                or_res = or_res | A[n - (j+2)]
        res = res ^ or_res
        ans = min(ans, res)
        #print("i = {}".format(i))
        #print(res)
    print(ans)

if __name__ == '__main__':
    main()