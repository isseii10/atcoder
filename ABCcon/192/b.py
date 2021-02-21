import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    s = input()[:-1]
    yes_flag = True
    for i in range(len(s)):
        if i % 2 == 0:
            if 0 <= ord(s[i]) - ord('a') <= 26:
                pass
            else:
                yes_flag = False
        else:
            if 0 <= ord(s[i]) - ord('A') <= 26:
                pass
            else:
                yes_flag = False
    if yes_flag:
        print("Yes")
    else:
        print("No")
    
if __name__ == '__main__':
    main()