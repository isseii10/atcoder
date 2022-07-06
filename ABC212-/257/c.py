import sys
from bisect import bisect_left
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    s = input()[:-1]
    w = list(map(int, input().split()))
    child = defaultdict(int)
    adult = defaultdict(int)
    child_num = 0
    adult_num = 0
    for i in range(n):
        if s[i] == "1":
            adult[w[i]] += 1
            adult_num += 1
        else:
            child[w[i]] += 1
            child_num += 1
    xs = set(w)
    xs = list(xs)
    xs.sort()
    xs.append(max(w)+1)
    clear_c = 0
    c_buf = 0
    clear_r = adult_num
    r_buf = 0
    ans = 0
    for x in xs:
        clear_c += c_buf
        clear_r -= r_buf
        c_buf = child[x]
        r_buf = adult[x]
        ans = max(ans, clear_c+clear_r)
    print(ans)

    







if __name__ == '__main__':
    main()