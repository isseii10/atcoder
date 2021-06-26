import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353

# (x, y)を通る傾きaの直線の切片計算
def calc_line(xy, a):
    x, y = xy
    b = y - a*x
    return (a, b)

# 2つの傾き切片から交点を計算
def calc_crosspoint(ab1, ab2):
    a1, b1 = ab1
    a2, b2 = ab2
    x = (b2-b1)/(a1-a2)
    y = a1*x + b1
    return (x, y)

def calc_area(left_point, right_point, al, ar, vi):
    xl, yl = left_point
    xr, yr = right_point
    al, bl = calc_line(left_point, al)
    ar, br = calc_line(right_point, ar)
    xc, yc = calc_crosspoint((al, bl), (ar, br))
    area = 0
    if xc < xl:
        area -= (yl - (xr-xl))**2 / 2
        area += (xr-xl)**2 / 2
    if 0 <= yc <= vi:
        area += (xc-xl)*yl + (xc-xl)*(yc-yl)/2
        area += (xr-xc)*yr + (xr-xc)*(yc-yr)/2
    else:
        xlc, ylc = calc_crosspoint((al, bl), (0, vi)) 
        xrc, yrc = calc_crosspoint((ar, br), (0, vi))
        area += (xlc - xl)*(vi-yl)/2 +(xlc-xl)*yl + (xrc-xlc)*vi + (xr-xrc)*(vi-yr)/2 + (xr-xrc)*yr
    return area 
    
def main():
    n = int(input())
    t = [0] + list(map(int, input().split()))
    v = list(map(int, input().split()))
    for i in range(1, n+1):
        t[i] += t[i-1]
    #print(t)
    """
    tはx座標
    vは区間（n個ある）の速度制限
    """
    left_right = [] #left_rightは区間iの左端の点と右端の点
    if n == 1:
        left_right.append(((0, 0), (t[1], 0)))
    else:
        left_right.append([(0, 0), (t[1], min(t[1]-t[0], v[0], v[1]))])
        for i in range(1, n-1):
            left_point = left_right[-1][1]
            right_point = (t[i+1], min(v[i], v[i+1]))
            left_right.append([left_point, right_point])
        left_right.append([left_right[-1][1], (t[-1], 0)])
    #print(left_right)
    ans = 0
    for i in range(n): # n-1個の区間について
        left, right = left_right[i]
        if left[1] == right[1] == v[i]:
            ans += (right[0] - left[0])*v[i]
            #print((right[0] - left[0])*v[i])
        else:
            #print(calc_area(left, right, 1, -1, v[i]))
            ans += calc_area(left, right, 1, -1, v[i])
    
    print("{:.10f}".format(ans))
        



        



if __name__ == '__main__':
    main()