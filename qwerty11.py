n = int(input())
i = int(1)

while i <= n:
    if n % i == 0:
        print(i, end=" ")
    i += 1
print()
for i in range (1 , n + 1):
    if n % i == 0:
        print(i, end=" ")
        
