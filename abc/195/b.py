import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    a, b, w = map(int, input().split())
    w *= 1000
    max_count = w / a
    min_count = w / b
    min_count = int(min_count)
    if w % b != 0:
        min_count += 1
    max_count = int(max_count)
    if min_count > max_count:
        print('UNSATISFIABLE')
    else:
        print(min_count, max_count)
    


if __name__ == '__main__':
    main()