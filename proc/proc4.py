def trianglePS(a):
    p = 3 * a
    s = a ** 2 * (3 / 4) ** 0.5
    return p, s
a = int(input())
print(trianglePS(a))
