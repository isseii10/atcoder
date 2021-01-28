"""
grundy数の実験用
grundy数が0のとき負けパターン
grundy数が0より大のとき勝ちパターン
(次の状態のgrundy数が0になるような操作が存在すれば。言い換えれば負けパターンを相手に押し付けることができれば。)

問題に応じてgrundy()の引数(key)と処理を変えて使う
今のgrundy()はatcoder ABC059D用
"""

import typing
from collections import defaultdict
def mex(xs: typing.List[int]) -> int:
    xs.sort()
    y = 0
    for x in xs:
        if y < x:
            break
        if y == x:
            y += 1
    
    return y


memo = defaultdict(int) #memoにはキー(盤面の状態)のgrundy数を入れる

def grundy(x, y) -> int: #キー(今回ABC057Dのキーは２変数)のgrundy数を返す

    #key(x, y)と(y, x)は同じ状態なので、x<yとなるようにしているだけ
    if x > y:
        key = (y, x)
    else:
        key = (x, y)

    
    if key not in memo.keys():
        # gには、keyの状態から遷移できる状態key'のグランディ数を再帰で求めて入れている
        g = []
        for i in range(2, x+1, 2):
            g.append(grundy(x-i, y+i//2))
        for i in range(2, y+1, 2):
            g.append(grundy(x+i//2, y-i))
        
        memo[key] = mex(g)
    
    return memo[key]

for x in range(100):
    for y in range(100):
        if grundy(x, y) == 0:
            print(x, y)
"""
printed:
0 0
0 1
1 0
1 1
1 2
2 1
2 2
2 3
3 2
3 3
...
この結果から、grundy数が０になるのは、|x-y| <= 1の時とわかる！！！
"""


"""
下のgrundy()はatcoder ABC027C倍々ゲーム用
"""
def grundy(x, n) -> int: 
    if x not in memo.keys():
        # gには、keyの状態から遷移できる状態key'のグランディ数を再帰で求めて入れている
        g = []
        if 2*x <= n:
            g.append(grundy(2*x, n))
        if 2*x + 1 <= n:
            g.append(grundy(2*x+1, n))
        
        memo[x] = mex(g)
    
    return memo[x]


for i in range(1, 500):
    memo = defaultdict(int)
    if grundy(1, i) == 0:
        print("{} :Aoki".format(i))
    else:
        print("{} :Takahashi".format(i))