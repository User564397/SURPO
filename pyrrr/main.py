def calc(a, b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)


a, b = list(map(int, input().split()))
calc(a, b)
