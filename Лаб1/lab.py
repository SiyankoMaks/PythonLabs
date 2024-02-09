# Сиянко Максим 37/1

# Вариант 11

# Задание 1: Составить 3 функции для работы с цифрами или делителями числа на основании варианта. Каждая функция - отдельный коммит

# Функция 1 Найти количество делителей числа, не делящихся на 3

def kol():
    k = 0
    a = int(input())
    for i in range(1, a + 1):
        if a % i == 0:
            if i % 3 == 0:
                k = k + 1
    return k

print(kol())

# Функция 2 Найти минимальную нечетную цифру числа

def numMin():
    num = 10
    a = int(input())
    while a != 0:
        b = a % 10
        if (b < num and b % 2 != 0):
            num = b
        a = a // 10
    return num

print(numMin())

# Функция 3 Найти сумму всех делителей числа, взаимно простых с суммой цифр числа и НЕ взаимнопростых с произведением цифр числа

def sumDel():
    a = int(input())
    sum = 0
    a_copy = a
    a_sum = 0
    a_pr = 1
    while a_copy != 0:
        a_sum += a_copy % 10
        a_pr *= a_copy % 10
        a_copy = a_copy // 10
    print(a_sum)
    print(a_pr)
    for i in range(2, a + 1):
        if a % i == 0:
            if a_sum % i != 0:
                if a_pr % i == 0:
                    sum += i
    return sum
print(sumDel())

# Задание 2-4

# 2(5). Дана строка. Необходимо перемешать все символы строки в случайном порядке.

def Tsk1():
    import random

    def new_string(s):
        return ''.join(random.sample(s, len(s)))

    st = "myText"
    new_st = new_string(st)
    print(new_st)

# 3(7). Дана строка, состоящая из символов латиницы. Необходимо проверить, образуют ли прописные символы этой строки палиндром.

def Tsk2():
    st = str(input())
    nst = st[::-1]
    if st == nst:
        print('Палиндром')
    else:
        print("НЕ палиндром")


# 4(14). Дана строка в которой записаны слова через пробел. Необходимо упорядочить слова по количеству букв в каждом слове

def Tsk3():
    st = str(input())
    newSt = st.split()
    newSt.sort(key=len)
    newSt = ' '.join(newSt)
    print(newSt)

print("Введите цифру 1, 2 или 3 для выбора задачи")
a = int(input())
if a==1: Tsk1()
elif a==2: Tsk2()
elif a==3: Tsk3()
else: print("Номер введен некорректно")
