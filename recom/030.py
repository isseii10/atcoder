n, m = map(int, input().split())
minute = m/60
if n>=12:
    n -= 12
hour = (n + m/60)/12
sa = abs(30*n - 5.5*m)
if sa > 180:
    sa = 360 - sa
print(sa)