n = int(input())
m = int(input())
i = int(n)

while i <= m:
    if i % 2 == 1:
        print(i, end=" ")
    i += 1

print()
for a in range(n, m + 1):
    if a % 2 == 1:
        print(a, end=" ")
