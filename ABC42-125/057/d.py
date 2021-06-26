import sys
from collections import deque, Counter
input = sys.stdin.readline
#sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353

import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def main():
    n, a, b = map(int, input().split())
    v = list(map(int, input().split()))
    v.sort()
    d = deque(v)
    value_list = []
    a_ = a
    x = 0
    while a_ > 0:
        x = d.pop()
        value_list.append(x)
        a_ -= 1
    value = sum(value_list)
    print("{:.10f}".format(value/a))

    c_v = Counter(v)
    c_value = Counter(value_list)
    ans = 0
    if a == c_value[x]:
        p = c_v[x]
        #今xをa個選んでいるが、min(p, b)個まで選べる
        for i in range(a, min(p, b)+1):
            ans += combinations_count(p, i)   

    else:
        p = c_v[x]
        q = c_value[x]
        #p個のxからq個選ぶ
        ans = combinations_count(p, q)

    print(ans)


if __name__ == '__main__':
    main()