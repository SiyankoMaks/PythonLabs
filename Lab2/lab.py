# Сиянко Максим 37/1

# Вариант 1

# Задание 1. Дан список чисел. Определите, сколько в нем встречается различных чисел.

print("Введите список чисел")
num_list = []
a = int(input())
while a != 0:
    num_list.append(a)
    a = int(input())
num_unique = len(set(num_list))
print(num_unique)