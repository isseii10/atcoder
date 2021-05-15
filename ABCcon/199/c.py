import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    s = list(input()[:-1])
    q = int(input())
    t2_flag = False
    for _ in range(q):
        t, a, b = map(int, input().split())
        a -= 1
        b -= 1
        if t == 1:
            if t2_flag:
                if a < n and b < n:
                    s[a+n], s[b+n] = s[b+n], s[a+n]
                elif a < n and n <= b:
                    s[a+n], s[b-n] = s[b-n], s[a+n]
                elif n <= a and b < n:
                    s[a-n], s[b+n] = s[b+n], s[a-n]
                else:
                    s[a-n], s[b-n] = s[b-n], s[a-n]
            else:
                s[a], s[b] = s[b], s[a]
        if t== 2:
            if t2_flag:
                t2_flag = False
            else:
                t2_flag = True
    if t2_flag:
        s = s[n:] + s[:n]
    print("".join(s)) 

if __name__ == '__main__':
    main()