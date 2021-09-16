n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

max_a = [0]*n
max_a[0] = a[0]
for i in range(n-1):
    max_a[i+1] = max(max_a[i], a[i+1])

c = [0]*n
c[0] = a[0] * b[0]
print(c[0])
for i in range(1, n):
    c[i] = max(c[i-1], max_a[i]*b[i])
    print(c[i])
