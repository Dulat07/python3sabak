array = []
a = 1
for i in range(3):
    array.append(int(input()))
    a = a * array[i]
print(a)
