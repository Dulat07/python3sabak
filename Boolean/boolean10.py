a, b = map(int, input().split())
result = (a % 2 == 1 and b % 2 == 0) or (a % 2 == 0 and b % 2 == 1)
print(result)