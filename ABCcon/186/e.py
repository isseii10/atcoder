def GCD(a, b):
    if a==0:
        return b
    return GCD(b%a, a)


'''
a*x + b*y = gcd(a, b)
gcdの再帰から、(b%a)*X + a*Y = gcd(a, b)が導かれる.
b%a + b//a*a = bより、
b%a*X = b*X - b//a*a*X
(b*X - b//a*a*X) + a*Y = gcd(a,b)
a*(Y - b//a*X) + b*X = gcd(a,b)
'''
# return (x, y, gcd(a,b)) 
def extGCD(a, b):
    if a==0: return (0, 1, b)

    (X, Y, g) = extGCD(b%a, a)
    return (Y-b//a*X, X, g)

t = int(input())
for _ in range(t):
    n, s, k = map(int, input().split())
    g = GCD(k, n)
    if s % g != 0:
        print(-1)
        continue
    s //= g
    k //= g
    n //= g
    x, y, G = extGCD(k, n)
    x *= (-s)
    x %= n
    print(x)
