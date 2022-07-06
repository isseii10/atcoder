import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    c = list(map(int, input().split()))
    c = [[c[i], i+1] for i in range(len(c))]
    c.sort()
    ans = ""
    def divide(n, ans, c):
        max_num = 0
        max_d = 0
        max_a = 0
        for i in range(9):
            ci, num = c[i]
            if n // ci >= max_d:
                if n % ci >= max_a:
                    if max_num <= num:
                        max_num = num
                        max_d = n // ci
                        max_a = n % ci
        ans += str(max_num)*max_d
        return max_a, ans
    
    while c[0][0] < n:
        n, ans = divide(n, ans, c)
    print(ans)
    

if __name__ == '__main__':
    main()