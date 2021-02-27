import sys
from math import gcd

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353

def count_2(x):
    count = 0
    while x % 2 == 0:
        x //= 2
        count += 1
    return count

def LCM(x, y):
    return x // gcd(x, y) * y

def main():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    #初め一回割っとく
    for i in range(n):
        A[i] //= 2
    

    count = count_2(A[0])
    lcm = 1
    for i in range(n):
        if count != count_2(A[i]):
            print(0)
            exit()
        A[i] //= 2**count
        lcm = LCM(lcm, A[i])


    for _ in range(count):
        m //= 2

    #今A[i]は奇数なので、Xも奇数
    #lcmの奇数倍がXになる
    max_p = m // lcm
    ans = (max_p + 1)//2
    print(ans)

    
if __name__ == '__main__':
    main()