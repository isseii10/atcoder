import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353

# mod使わない
# 遅いやつ
import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def main():
    A, B, K = map(int, input().split())

    ans = ""

    while A > 0 and B > 0:
        use_a = combinations_count(A+B-1, A-1)
        if K > use_a:
            ans += 'b'
            B -= 1
            K -= use_a

        else:
            ans += 'a'
            A -= 1

            
    
    ans += 'a' * A
    ans += 'b' * B 
    print(ans)





    
if __name__ == '__main__':
    main()