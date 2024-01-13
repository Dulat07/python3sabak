array = []
n = int(input())
k = int(input())
bar_ma = False
for i in range(n):
    array.append(int(input()))
    if array[i] < k:
        bar_ma = True
print(bar_ma)