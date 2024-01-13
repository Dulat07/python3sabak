array = []
n = int(input())
sum = 1

for i in range(n):
    array.append(float(input()))
    sum *= array[i] - int(array[i])
print(sum)
