a = int(input())
b = int(input())

x = (a % 2 == 1 and b % 2 == 1) or (a % 2 == 0 and b % 2 == 0)
print(x)