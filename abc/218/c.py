import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353

def turn_90(s):
    y = len(s)
    x = len(s[0])
    ret = [["."] * y for _ in range(x)]
    for i in range(y):
        for j in range(x):
            ret[j][y-1-i] = s[i][j]
    return ret

def main():
    n = int(input())
    s = [list(input()[:-1]) for _ in range(n)]
    t = [list(input()[:-1]) for _ in range(n)]
    
    def del_yohaku(s):
        flag = False
        ret = []
        for line in s:
            m = len(line)
            dots = ["."]*m
            for c in line:
                if c == "#":
                    flag=True
                    break
            if flag:
                ret.append(line)
        return ret
    
    for _ in range(4):
        s = turn_90(s)
        s = del_yohaku(s)
        t = turn_90(t)
        t = del_yohaku(t)
    
    #print(s)
    #print(t)
    
    for _ in range(4):
        y_s = len(s)
        x_s = len(s[0])
        y_t = len(t)
        x_t = len(t[0])

        #print("++++++++++++++++++++++++++++++")
        #for i in range(y_s):
        #    print(s[i])
        #for i in range(y_t):
        #    print(t[i])
        #print("++++++++++++++++++++++++++++++")
        
        ok = True
        if y_t == y_s and x_s == x_t:
            for i in range(y_s):
                for j in range(x_s):
                    if s[i][j] != t[i][j]:
                        ok = False
                        break
                if not ok:
                    break
            
            if ok:
                print("Yes")
                exit()
        
        s = turn_90(s)

    print("No")
                
if __name__ == '__main__':
    main()