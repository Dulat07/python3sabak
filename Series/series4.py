array = []
n = int(input("Enter size of array \n"))
sum = 0
for i in range(n):
    array.append(int(input()))
    sum += array[i]

print(sum)