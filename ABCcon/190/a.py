import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353

def check_array(array):
    print('array is')
    for i in range(len(array)):
        print(array[i])


def main():
    a, b, c = map(int, input().split())
    if a==b:
        if c == 0:
            print("Aoki")
        else:
            print("Takahashi")
    else:
        if a < b:
            print("Aoki")
        else:
            print("Takahashi")
if __name__ == '__main__':
    main()