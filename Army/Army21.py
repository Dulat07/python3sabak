x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())

AB = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
AC = (((x3 - x1) ** 2) + ((y3 - y1) ** 2)) ** 0.5
BC = (((x1 - x3) ** 2) + ((y1 - y3) ** 2)) ** 0.5

p = (AB + AC + BC) / 2
S = (p * (p - AB) * (p - AC) * (p - BC)) ** 0.5
if (AB + AC) > BC and (AB + BC) > AC and AB < (AC + BC):
    print(S)
else:
    print("lox")
