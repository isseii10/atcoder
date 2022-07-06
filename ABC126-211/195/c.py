import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n_str = input()[:-1]
    digit = len(n_str)
    comma = (digit-1) // 3
    if comma == 0:
        print(0)
        exit()

    ans = 0
    k = 1000
    for i in range(1, comma+1):
        n_former, n_later  = n_str[:(-3*i)], n_str[(-3*i):]
        #print(n_former, n_later)
        ans += (int(n_former)-1)*k + int(n_later)+1
        k *= 1000
    print(ans)


    
if __name__ == '__main__':
    main()