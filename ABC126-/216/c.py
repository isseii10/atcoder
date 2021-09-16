import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    n_bit = ""
    while n > 0:
        if n % 2 == 1:
            n_bit = "1" + n_bit 
        else:
            n_bit = "0" + n_bit
        n //= 2

    #print(n_bit)

    ans = ""
    one_flag = False
    for i in range(len(n_bit)-1):
        if n_bit[i] == "1":
            ans += "AB"
        else:
            ans += "B"
    
    if n_bit[-1] == "1":
        ans += "A"
    print(ans)
if __name__ == '__main__':
    main()