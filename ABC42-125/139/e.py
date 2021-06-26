import sys
import copy
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353



def main():
    n = int(input())
    A = [list(map(int, input().split())) for _ in range(n)]
    ques = [deque(A[i]) for i in range(n)]

    day = 0
    finish_all = [False]*n
    yesterday = [True]*n

    q = deque()
    for a in range(n):
        b = ques[a].popleft()
        a_ = ques[b].popleft()
        if a_ == a:
            if a > b:
                a, b = b, a
            q.append((a, b))
        else:
            ques[a].appendleft(b)
            ques[b].appendleft(a_)

    seen = set()
    while q:
        pair = q.popleft()
        if pair in seen:continue


        


    print(day)

    
if __name__ == '__main__':
    main()