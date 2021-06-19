import sys
from collections import defaultdict, Counter

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353
def fctr_d(n):
    c = 0
    r = int(n**0.5)
    f = defaultdict(int)
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
    l, r = map(int, input().split())
    prime_dict = dict(list)
    for i in range(l, r+1):
        prime_count = fctr_d(i)
        prime_set = set(prime_count.keys())
        prime_dict[i] = [prime_set, prime_count]
    
    



if __name__ == '__main__':
    main()