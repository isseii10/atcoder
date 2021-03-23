import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    n_str = str(n)
    digit = len(n_str)
    ans = 0
    for i in range(2, digit+1)[::2]:
        if i < digit:
            ans += 9 * 10**(i//2 - 1)
        else:
            n_first = n_str[:digit//2]
            n_second = n_str[digit//2:]
            n_first = int(n_first)
            n_second = int(n_second)

            if n_first <= n_second:
                    ans += 1

            res = n_first - 10**(digit//2-1)
            ans += res
    print(ans)

    
if __name__ == '__main__':
    main()