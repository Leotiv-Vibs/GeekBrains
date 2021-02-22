n = [111, 222, 333, 444, 555, 666, 777, 0]

def first():
    max_s = 0
    max_m = 0
    for i in n:
        m = i
        s = 0
        while i > 0:
            s += i % 10
            i //= 10
        if s > max_s:
            max_s = s
            max_m = m
    return max_m, max_s

def second(n):
    max_s = 0
    max_m = 0
    if n == 0:
        return max_s, max_m

