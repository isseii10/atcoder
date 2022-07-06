
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    a, b, c, d = map(int, input()[:-1].split())

    if a < c:
        print("Takahashi")
    elif a > c:
        print("Aoki")
    else:
        if b <= d:
            print("Takahashi")
        else:
            print("Aoki") 




    
if __name__ == '__main__':
   main()