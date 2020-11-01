
def fact(n):
    factorial = 1
    for i in range(1, n+1):
        print(i)
        factorial *= i
    yield factorial


for el in fact(4):
    print(el)
