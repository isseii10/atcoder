import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    s = input()[:-1]
    k = int(input())
    cleaned = set()
    now_x = 0
    now_y = 0
    cleaned.add((0, 0))
    move = dict()
    move['R'] = (1, 0)
    move['L'] = (-1, 0)
    move['U'] = (0, -1)
    move['D'] = (0, 1)
    for c in s:
        dx, dy = move[c]
        now_x = now_x + dx 
        now_y = now_y + dy
        cleaned.add((now_x, now_y))
    ans1 = len(cleaned)
    for c in s:
        dx, dy = move[c]
        now_x = now_x + dx 
        now_y = now_y + dy
        cleaned.add((now_x, now_y))
    ans2 = len(cleaned)
    d_ans = ans2 - ans1
    


        
if __name__ == '__main__':
    main()