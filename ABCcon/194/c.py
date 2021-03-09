import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    A = list(map(int, input().split()))
    sa = [0]*(n+1)
    sa_2 = [0]*(n+1)
    for i in range(n):
        sa[i+1] = sa[i] + A[i]
        sa_2[i+1] = sa_2[i] + A[i]**2
    #print(sa)
    #print(sa_2)

    A = [0] + A

    ans = 0
    for i in range(2, n+1):
        res = (i-1)*A[i]**2 - 2*A[i]*sa[i-1] + sa_2[i-1]
        ans += res
        #print("i= {}".format(i))
        #print(res)
    print(ans)

    
if __name__ == '__main__':
    main()