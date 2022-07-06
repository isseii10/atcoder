import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    ss = [input()[:-1] for _ in range(4)]
    check = dict()
    _H = 0
    _2B = 0
    _3B = 0
    _HR = 0
    for s in ss:
        if s == "H":
            _H += 1
        if s == "2B":
            _2B += 1
        if s == "3B":
            _3B += 1
        if s == "HR":
            _HR += 1
        if _H > 1 or _2B > 1 or _3B > 1 or _HR > 1:
            print("No")
            exit()
    print("Yes")

if __name__ == '__main__':
    main()