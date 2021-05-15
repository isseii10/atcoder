import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    s = input()[:-1]
    t = deque()
    flag = 0
    for c in s:
        if c == 'R':
            flag = 1-flag
        else:
            if len(t) == 0:
                t.append(c)
                continue

            if flag:
                if t[0] == c:
                    t.popleft()
                else:
                    t.appendleft(c)
            else:
                if t[-1] == c:
                    t.pop()
                else:
                    t.append(c)
    res = []
    if flag:
        for i in range(len(t))[::-1]:
            res.append(t[i])
    else:
        res = t
    print(''.join(res))

    

    



if __name__ == '__main__':
    main()