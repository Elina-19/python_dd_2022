history = {
    '+': [],
    '-': [],
    '*': [],
    '/': []
}


def calculate(arg1, arg2, sign):
    match sign:
        case '+':
            return arg1 + arg2
        case '-':
            return arg1 - arg2
        case '*':
            return arg1*arg2
        case '/':
            return arg1/arg2
        case _:
            return "Command is not valid"


def write_to_history(sign, str):
    history.get(sign).append(str)


while True:
    arg1 = int(input("Введите значение: "))
    arg2 = int(input("Введите значение: "))
    sign = input("Введите операцию: ")

    result = "{0} {1} {2} = {3}".format(arg1, sign, arg2, calculate(arg1, arg2, sign))
    print(result)
    write_to_history(sign, result)

    for key, value in history.items():
        print("{0} {1}".format(key, value))

