import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    deg, dis = map(int, input().split())
    ans_deg = ""
    if 112.5 <= deg < 337.5:
        ans_deg = "NNE"
    elif 337.5 <= deg < 562.5:
        ans_deg = "NE"
    elif 562.5 <= deg < 787.5:
        ans_deg = "ENE"
    elif 787.5 <= deg < 1012.5:
        ans_deg = "E"
    elif 1012.5 <= deg < 1237.5:
        ans_deg = "ESE"
    elif 1237.5 <= deg < 1462.5:
        ans_deg = "SE"
    elif 1462.5 <= deg < 1687.5:
        ans_deg = "SSE"
    elif 1687.5 <= deg < 1912.5:
        ans_deg = "S"
    elif 1912.5 <= deg < 2137.5:
        ans_deg = "SSW"
    elif 2137.5 <= deg < 2362.5:
        ans_deg = "SW"
    elif 2362.5 <= deg < 2587.5:
        ans_deg = "WSW"
    elif 2587.5 <= deg < 2812.5:
        ans_deg = "W"
    elif 2812.5 <= deg < 3037.5:
        ans_deg = "WNW"
    elif 3037.5 <= deg < 3262.5:
        ans_deg = "NW"
    elif 3262.5 <= deg < 3487.5:
        ans_deg = "NNW"
    else:
        ans_deg = "N"
    
    dis *= 10
    dis /= 60
    dis = str(dis)
    #print(dis)
    i, f = dis.split(".")
    i = int(i)
    #print(i, f)
    if 5 <= int(f[0]):
        i += 1

    i = int(i)
    #print(i)
    ans_dis = 0
    if 0 <= i <= 2:
        ans_deg = "C"
    elif 3 <= i <= 15:
        ans_dis = 1
    elif 16 <= i <= 33:
        ans_dis = 2
    elif 34 <= i <= 54:
        ans_dis = 3
    elif 55 <= i <= 79:
        ans_dis = 4
    elif 80 <= i <= 107:
        ans_dis = 5
    elif 108 <= i <= 138:
        ans_dis = 6
    elif 139 <= i <= 171:
        ans_dis = 7
    elif 172 <= i <= 207:
        ans_dis = 8
    elif 208 <= i <= 244:
        ans_dis = 9
    elif 245 <= i <= 284:
        ans_dis = 10
    elif 285 <= i <= 326:
        ans_dis = 11
    elif 327 <= i:
        ans_dis = 12

    print(ans_deg, ans_dis)
    
if __name__ == '__main__':
    main()