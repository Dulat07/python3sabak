product = 0
a,b = map(int, input().split())
for i in range(a, b + 1):
    product += i ** 2
print(product)
