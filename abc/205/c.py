import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    A, B, C = map(int, input().split())
    if A == B:
        print("=")
        exit()
    
    if C % 2 == 1:
        if (A <= 0 and B <= 0) or (A > 0 and B > 0):
            if A < B:
                print("<")
            else:
                print(">")
        elif A <= 0 and B > 0:
            print("<")

        elif A > 0 and B <= 0:
            print(">")


    else:
        if abs(A) == abs(B):
            print("=")
        elif abs(A) < abs(B):
            print("<")
        else:
            print(">")

if __name__ == '__main__':
    main()