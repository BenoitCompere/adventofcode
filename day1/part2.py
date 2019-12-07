from part1 import f1

def f2(m):
    x = f1(m)
    if x > 0:
        x += max(f2(x), 0)
    return x
