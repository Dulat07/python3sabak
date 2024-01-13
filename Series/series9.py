array = []
n = int(input())
k = 0


for i in range(n):
    array.append(int(input()))
    if array[i] % 2 == 1:
        k += 1
print(k)