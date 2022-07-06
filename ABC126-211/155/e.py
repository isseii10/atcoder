from collections import Counter
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    s = input()[:-1]
    n = len(s)

    ans = 0
    carry = 0
    carry_5 = 0
    for i in range(n)[::-1]:
        x = int(s[i])
        if not (carry_5 == 1 and x < 5):
            x += carry_5
        
        x += carry

        if x == 10:
            carry = 1
            carry_5 = 0
            continue

        if x < 5:
            ans += x
            carry = 0
            carry_5 = 0
        elif x > 5:
            ans += 10 - x
            carry = 1
            carry_5 = 0
        else:
            ans += x
            carry = 0
            carry_5 = 1
    
    if carry == 1:
        ans += 1
    
    print(ans)


if __name__ == '__main__':
    main()