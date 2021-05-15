import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    skills = []
    for _ in range(n):
        skill = list(map(int, input().split()))
        skills.append(skill)
    dp = [[[0]*5 for _ in range(4)] for _ in range(n+1)]
    #dp[i][k]はi番目までみて、kにんチームの時

    for i in range(n):
        skill_i = skills[i]
        for j in range(5):
            dp[i+1][3][j] = max(dp[i][2][j], skill_i[j])
            dp[i+1][2][j] = max(dp[i][1][j], skill_i[j])
        if min(dp[i][1]) < min(skill_i):
            dp[i+1][1] = skill_i
        else:
            dp[i+1][1] = dp[i][1]
        
    for i in range(n+1):
        print(dp[i])
    ans = 0
    for i in range(1, n+1):
        ans = max(ans, min(dp[i][3]))
    print(ans)



    
if __name__ == '__main__':
    main()