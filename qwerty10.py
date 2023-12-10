n = int(input())
m = int(input())
i = int(n)

while i <= m:
    if i % 3 == 0:
        print(i, end=" ")
    i += 1
print()
for i in range(n, m + 1):
    if i % 3 == 0:
        print(i, end=" ")
