ls = list(map(int, input().split()))

print("Список четных чисел: ", [i for i in ls if i % 2 == 0])
print("Список нечетных чисел: ", [i for i in ls if i % 2 != 0])
print("Список чисел меньше 0: ", [i for i in ls if i < 0])

print("Список четных чисел: ", list(filter(lambda x: x % 2 == 0, ls)))
print("Список нечетных чисел: ", list(filter(lambda x: x % 2 != 0, ls)))
print("Список чисел меньше 0: ", list(filter(lambda x: x < 0, ls)))
