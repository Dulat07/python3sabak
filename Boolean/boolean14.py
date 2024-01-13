a, b, c = map(int, input().split())
result = (a > 0 and b < 0 and c < 0) or (a < 0 and b > 0 and  c < 0) and (a < 0 and b < 0 and c > 0)
print(result)