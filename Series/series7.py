array = []
n = int(input())
sum = 0

for i in range(n):
    array.append(float(input()))
    sum += round(array[i])
print(sum)