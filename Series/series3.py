array = []
sum = 0
counter = 0
for i in range(3):
    array.append(int(input()))
    counter += 1
    sum += array[i]

print(sum / counter)