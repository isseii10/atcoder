import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n, m, q = map(int, input().split())
    nimotu = []
    for _ in range(n):
        w, v = map(int, input().split())
        nimotu.append((v, w))
    nimotu.sort(reverse=True)

    X = list(map(int, input().split()))



    for _ in range(q):
        l, r = map(int, input().split())
        l -= 1
        box = X[:l] + X[r:]
        if len(box) == 0:
            print(0)
            continue

        box.sort()
        seen_box = [False]*len(box)
        ans = 0
        for v, w in nimotu:
            flag = False
            for i in range(len(box)):
                if flag:
                    break
                if box[i] >= w:
                    if not seen_box[i]:
                        seen_box[i] = True
                        ans += v
                        flag = True
                else:
                    continue
        print(ans)


    
if __name__ == '__main__':
    main()