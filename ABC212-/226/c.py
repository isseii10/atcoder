import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353

def main():
    n = int(input())
    tka = [list(map(int, input().split())) for _ in range(n)]

    
    ans = 0
    waza_ok = [False]*n
    def dfs(waza_p, ans):
        if waza_ok[waza_p-1]:return ans
        if tka[waza_p-1][1] != 0:
            for waza_c in tka[waza_p-1][2:]:
                if waza_ok[waza_c-1]:
                    continue
                ans = dfs(waza_c, ans)
        waza_ok[waza_p-1] = True
        ans += tka[waza_p-1][0]
        return ans 

    ans = dfs(n, ans)
    print(ans)
        
        
if __name__ == '__main__':
    main()