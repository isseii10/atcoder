n = int(input())
t = input()

loop = n//3
s_unit = ""
if n%3!=0:
    for i in range(loop + 1):
        s_unit += "110"
else:
    for i in range(loop):
        s_unit += "110"

ans1 = s_unit.count(t)
if ans1 == 0:
    s_unit += "110"
    ans1 = s_unit.count(t)
    loop += 1

print(ans1*(10000000000 - (len(s_unit)//3 -1)))