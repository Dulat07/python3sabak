array = []
n = int(input())
k = 0
bar_ma = False
for i in range(n):
    array.append(int(input()))
    if array[i] > 0:
        bar_ma = True
print(bar_ma)