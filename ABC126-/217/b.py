import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    contests = dict()
    contests["ABC"] = False
    contests["ARC"] = False
    contests["AGC"] = False
    contests["AHC"] = False
    for _ in range(3):
        s = input()[:-1]
        contests[s] = True
    
    for c, bool in contests.items():
        if not bool:
            print(c)
            exit()
if __name__ == '__main__':
    main()