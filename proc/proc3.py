def mean(x, y):
    Amean = (x + y) / 2
    Gmean = (x * y) ** 0.5
    return Amean, Gmean

x = int(input())
y = int(input())
print(mean(x, y))