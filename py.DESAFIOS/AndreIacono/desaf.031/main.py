def facto(n):
    f = 1

    for i in range(1, n + 1):
        f *= i
    return f


print(facto(10))
