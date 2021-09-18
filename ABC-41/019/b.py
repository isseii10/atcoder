import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    s = input()[:-1]
    n = len(s)
    count = 1
    ans = ""
    for i in range(n-1):
        if s[i] == s[i+1]:
            count += 1
        else:
            count_str = str(count)
            ans += s[i] + count_str
            count = 1
    ans += s[-1] + str(count)
    print(ans)
    
if __name__ == '__main__':
    main()