def RectPS(x1, y1, x2, y2):
    a = x2 - x1
    b = y2 - y1
    S = a * b
    P = 2 * (a + b)
    return S, P
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
print(RectPS(x1, y1, x2, y2))