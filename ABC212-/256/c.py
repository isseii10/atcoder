import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    lines = [set() for _ in range(3)]
    def calc(hx, line_num):
        for i11 in range(1, hx+1):
            nokori = max(0, hx-i11)
            for i12 in range(1, nokori+1):
                i13 = nokori - i12
                if i13 < 1:continue
                lines[line_num].add((i11, i12, i13))
    calc(h1, 0)
    calc(h2, 1)
    calc(h3, 2)
    ans = 0
    for line1 in lines[0]: # 900
        for line2 in lines[1]: #900
            i11, i12, i13 = line1
            i21, i22, i23 = line2
            i31 = w1 - i11 - i21
            i32 = w2 - i12 - i22
            i33 = w3 - i13 - i23
            if i31 < 1 or i32 < 1 or i33 < 1:continue
            if (i31, i32, i33) in lines[2]:
                ans += 1
    print(ans)

            


if __name__ == '__main__':
    main()