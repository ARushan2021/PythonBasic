numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]

def f(x):
    for y in range(0, x):
        if x%2 != 0 and x > 50: return 1
    return 0
print(list(filter(f, numbers)))