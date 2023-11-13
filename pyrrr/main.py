def print_hi(name):
    print(f'Hi, {name}')


def calc(a, b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)


if __name__ == '__main__':
    name = input('Введте своё имя: ')
    print_hi(name)
    a, b = list(map(int, input().split()))
    calc(a, b)

    print('Введите 2 числа через пробел: ')
    a, b = list(map(int, input().split(' ')))
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
