class S:
    def __init__(s, n):
        s.n = n

    def b(s, t):
        l = 0
        r = len(s.n) - 1
        while l <= r:
            m = (l + r) // 2
            if s.n[m] == t:
                return m
            elif s.n[m] < t:
                l = m + 1
            else:
                r = m - 1
        return -1

def f():
    a = [2, 4, 6, 8, 10, 12, 14]
    t = 10
    s = S(a)
    i = s.b(t)
    print("Found at index:", i)

f()
