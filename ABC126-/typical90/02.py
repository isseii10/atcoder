import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    ans = []
    if n % 2 == 1:
        print("")
        exit()
    
    for i in range(1 << n):
        res = ""
        count = 0
        for j in range(n):
            if i >> j & 1:
                res += "("
                count += 1
            else:
                res += ")"
                count -= 1

            if count < 0:
                break
        else:
            if count == 0:
                ans.append(res)
    
    ans.sort()
    for a in ans:
        print(a)

if __name__ == '__main__':
    main()