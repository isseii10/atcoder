from collections import deque
n = int(input())
s = input()
f_count = 0
fo_count = 0
minus = 0
d = deque()
for i in range(n):
    if s[i]!="f" and s[i] !="o" and s[i] != "x":
        d = deque()
    if s[i] == "f":
        d.append(1)
    if s[i] == "o":
        if d:
            if d[-1] == 1:
                d.pop()
                d.append(2)
            else:
                d = deque()
    if s[i] == "x":
        if d:
            if d[-1] == 2:
                d.pop()
                minus += 3
            else:
                d = deque()
print(n-minus)