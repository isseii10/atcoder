import sys
import bisect
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353

#n以下の素数列挙(O(n log(n))
def primes(n):
    ass = []
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    for i in range(len(is_prime)):
        if is_prime[i]:
            ass.append(i)
    return ass

def main():
    n = int(input())
    prime_list = primes(1000000)
    prime_list.sort()
    #print(prime_list)
    #print(len(prime_list)*(len(prime_list)-1)//2)
    ans = 0
    for idx_q, q in enumerate(prime_list):
        q3 = q**3
        if q3 >= n:
            continue
        max_p = n // q3
        #if max_p == 1:
        #    continue
        #print(max_p, q)
        idx_p = bisect.bisect_right(prime_list, max_p)
        #print("q is {}".format(q))
        #print("prime_list[idx_p] is {}, idx_p is {}".format(prime_list[idx_p], idx_p))
        
        ans += min(idx_p, idx_q)
    print(ans)
        
        

if __name__ == '__main__':
    main()