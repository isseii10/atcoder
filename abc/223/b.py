import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    s = input()[:-1]
    ss = s + s
    s_list = []
    for i in range(len(s)):
        s_list.append(ss[i:i+len(s)])
    s_list.sort()
    print(s_list[0])
    print(s_list[-1])
if __name__ == '__main__':
    main()