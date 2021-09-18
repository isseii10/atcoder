import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    s = input()[:-1]
    str_Do = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Si']
    list_Kenban = []
    Do = 'WBWBWWBWBWBW'
    m = len(Do)

    for i in range(m):
        if Do[i] == 'W':
            tmp = Do[i:] + Do[:i]
            list_Kenban.append(tmp)

    dict_ans = dict()
    for kenban, do in zip(list_Kenban, str_Do):
        dict_ans[kenban] = do

    print(dict_ans[s[:m]]) 

if __name__ == '__main__':
    main()