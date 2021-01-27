# 1-dimension Rolling Hash
#base = 37 mod = 10**9 + 9
class RollingHash():
    def __init__(self, s, base, mod):
        self.mod = mod
        self.pw = pw = [1] * (len(s) + 1)

        l = len(s)
        self.h = h = [0] * (l + 1)

        v = 0
        for i in range(l):
            h[i + 1] = v = (v * base + ord(s[i])) % mod
        v = 1
        for i in range(l):
            pw[i + 1] = v = v * base % mod

    def get(self, l, r):
        return (self.h[r] - self.h[l] * self.pw[r - l]) % self.mod


# 非クラス版
base = 37
mod = 10 ** 9 + 9
pw = None


def rolling_hash(s):
    l = len(s)
    h = [0] * (l + 1)
    v = 0
    for i in range(l):
        h[i + 1] = v = (v * base + ord(s[i])) % mod
    return h


# RH前に、必要な長さの最大値分のpow-tableを計算しておく
def setup_pw(l):
    global pw
    pw = [1] * (l + 1)
    v = 1
    for i in range(l):
        pw[i + 1] = v = v * base % mod


def get(h, l, r):
    return (h[r] - h[l] * pw[r - l]) % mod


# Random Rolling Hash
import random, math

random.seed()


def gen(a, b, num):
    result = set()
    while 1:
        while 1:
            v = random.randint(a, b) // 2 * 2 + 1
            if v not in result:
                break
        for x in range(3, int(math.sqrt(v)) + 1, 2):
            if v % x == 0:
                break
        else:
            result.add(v)
            if len(result) == num:
                break
    return result


class RH():
    def __init__(self, s, base, mod):
        self.base = base
        self.mod = mod
        self.rev = pow(base, mod - 2, mod)

        l = len(s)
        self.h = h = [0] * (l + 1)
        tmp = 0
        for i in range(l):
            num = ord(s[i])
            tmp = (tmp * base + num) % mod
            h[i + 1] = tmp

    def calc(self, l, r):
        return (self.h[r] - self.h[l] + self.mod) * pow(self.rev, l, self.mod) % self.mod


class RRH():
    def __init__(self, s, num=10):
        # 2 ~ 1000の間の乱数でnum個のハッシュをとる
        param = (2, 10 ** 3, num)
        MOD = 10 ** 9 + 7
        self.rhs = [RH(s, p, MOD) for p in gen(*param)]

    def calc(self, l, r):
        return [rh.calc(l, r) for rh in self.rhs]


# usage: RRH("abcd")

mod = 10 ** 9 + 9;
p = 13;
q = 19

p_table = q_table = None


def prepare(L):
    global p_table, q_table
    p_table = [1] * (L + 1);
    q_table = [1] * (L + 1)
    for i in range(L):
        p_table[i + 1] = p_table[i] * p % mod
        q_table[i + 1] = q_table[i] * q % mod


def rolling_hash(S, W, H):
    D = [[0] * (W + 1) for i in range(H + 1)]
    for i in range(H):
        su = 0
        dp = D[i]
        di = D[i + 1]
        si = S[i]
        for j in range(W):
            v = si[j]  # v = ord(si[j]) if si[j] is str
            su = (su * p + v) % mod
            di[j + 1] = (su + dp[j + 1] * q) % mod
    return D


def get(S, x0, y0, x1, y1):
    P = p_table[x1 - x0];
    Q = q_table[y1 - y0]
    return (S[y1][x1] - S[y1][x0] * P - S[y0][x1] * Q + S[y0][x0] * (P * Q) % mod) % mod


# example
data1 = [
    [1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [0, 1, 1, 1, 1],
]
data2 = [
    [1, 0, 1],
    [1, 0, 1],
]
prepare(L=5)
rh1 = rolling_hash(data1, 5, 3)
rh2 = rolling_hash(data2, 3, 2)
print(get(rh1, 2, 0, 5, 2) == get(rh2, 0, 0, 3, 2))
# => "True"