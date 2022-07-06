import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    xs = input()[:-1]
    x_1 = xs[0]
    for i in range(1, 4):
        if xs[i] != x_1:
            break
    else:
        print("Weak")
        exit()
    
    for i in range(3):
        next_x = int(xs[i+1])
        now_x = int(xs[i])
        if next_x != (now_x + 1) % 10:
            break
    else:
        print("Weak")
        exit()
    
    print("Strong")

if __name__ == '__main__':
    main()