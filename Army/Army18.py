a = int(input())
b = int(input())
c = int(input())
s = a + b + c
if a > c > b:
    print(s - (c + b),s - (a + c))
else:
    print("A men B arasy")
