import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353

from collections import defaultdict
f = defaultdict(int)
def fctr_d(n):
    c = 0
    r = int(n**0.5)
    for i in range(2, r+2):
        while n % i == 0:
            c += 1
            n = n//i
        if c != 0:
            f[i] += c
            c = 0
    if n != 1:
        f[n] += 1
    return f

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    for num in a:
        f = fctr_d(num)
    #print(f)

    used = [1]*(m+1)
    used[0] = 0

    for k in f.keys():
        #print(k)
        base = k
        while k <= m:
            used[k] = 0
            k += base
        #print(used)
    print(sum(used))
    for i in range(1, m+1):
        if used[i] == 1:
            print(i) 

    
    
if __name__ == '__main__':
    main()