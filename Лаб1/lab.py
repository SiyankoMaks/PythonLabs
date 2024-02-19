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

# Задание 5: Дана строка. Необходимо найти все даты, которые описаны в виде "31 февраля 2007"

import re

text = str(input())
pattern = r'\b\d{1,2}\s(?:января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)\s\d{4}\b'
dates = re.findall(pattern, text)
print(dates)

# Задание 6-8

#6(5). Дана строка. Необходимо найти наибольшее количество идущих подряд символов кириллицы.

def maxSymb():
    st = str(input())
    xTime = 'aa'
    cur_lng = 0
    max_lng = 0
    for x in st:
        if xTime == x:
            cur_lng += 1
            if max_lng < cur_lng:
                max_lng = cur_lng
        else:
            cur_lng = 0
        xTime = x
    max_lng += 1
    print(max_lng)

#7(7). Дана строка. Необходимо найти минимальное из имеющихся в ней натуральных чисел.

def minMumber():
    st = str(input())
    newSt = st.split()
    minNum = 0.1
    for x in newSt:
        x = int(x)
        if minNum == 0.1:
            minNum = x
        if minNum > x:
            minNum = x
    print(minNum)

#8(14). Дана строка. Необходимо найти все используемые в ней строчные символы латиницы.

def strSymb():
    st = str(input())
    for s in st:
        if s.islower():
            print(s)

print("Введите цифру 1, 2 или 3 для выбора задачи")
a = int(input())
if a == 1: maxSymb()
elif a == 2: minMumber()
elif a == 3: strSymb()
else: print("Номер введен некорректно")

# Задание 9. Прочитать список строк с клавиатуры. Упорядочить по длине сткоки.

print("Введите список строк")
strings = []
st = input()
while(st):
    strings.append(st)
    st = input()
for i in range(0, len(strings)-1):
    for j in range(i+1, len(strings)):
        if(len(strings[i])>len(strings[j])):
            strings[i], strings[j] = strings[j], strings[i]
print(strings)

# Задание 10. Дан список строк с клавиатуры. Упорядочить по количеству слов в строке

print("Введите список строк")
strings = []
st = input()
while(st):
    strings.append(st)
    st = input()
for i in range(0, len(strings)-1):
    for j in range(i+1, len(strings)):
        if(len(strings[i].split()) > len(strings[j].split())):
            strings[i], strings[j] = strings[j], strings[i]
print(strings)

# Задание 11-14. Вариант 11. Задачи 2, 6, 9, 12. Отсортировать строки в указанном порядке.

# 11(2). В порядке увеличения среднего веса ASCII-кода символа строки.

def sortString(s):
    N = len(s)
    freq = [0] * 256
    for i in range(0, N):
        freq[ord(s[i])] += 1
    s = ""
    for i in range(256):
        for j in range(freq[i]):
            s = s + chr(i)
    print(s)
    return
print("Введите строку")
S = str(input())
sortString(S)

# 12(6). В порядке увеличения медианного значения выборки строк (прошлое
# медианное значение удаляется из выборки и производится поиск нового медианного значения)

def find_median(strk):
    strk = strk.split()
    sorted_numbers = sorted(map(int, strk))
    length = len(sorted_numbers)
    middle = length // 2
    if length % 2 == 0:
        median = (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
    else:
        median = sorted_numbers[middle]
    return median

print("Введите список строк")
strings = []
newstr = []
st = input()
while st:
    strings.append(st)
    st = input()
for i in range(len(strings)):
    newstr.append(find_median(strings[i]))
for i in range(1, len(strings)):
    if newstr[i-1] > newstr[i]:
        t1 = newstr[i-1]
        newstr[i-1] = newstr[i]
        newstr[i] = t1
        t2 = strings[i-1]
        strings[i-1] = strings[i]
        strings[i] = t2
print(strings)

# 13(9). В порядке увеличения квадратичного отклонения между наибольшим
# ASCII-кодом символа строки и разницы в ASCII-кодах пар зеркально
# расположенных символов строки (относительно ее середины).

def square_deviation(s):
    n = len(s)
    mid = n // 2
    max_ascii = max(ord(char) for char in s)
    mirror_diff = [abs(ord(s[i]) - ord(s[n - 1 - i])) for i in range(mid)]
    deviation = max_ascii - sum(mirror_diff) / len(mirror_diff)
    return deviation

print("Введите список строк")
strings = []
st = input()
while st:
    strings.append(st)
    st = input()
sorted_strings = sorted(strings, key=lambda x: square_deviation(x))
print(sorted_strings)

# 14(12). В порядке увеличение квадратичного отклонения частоты
# встречаемости самого распространенного символа в наборе строк от частоты его встречаемости в данной строке.

import math

def maxNum(st):
    max = -1
    kol = 0
    for i in range(1, len(st)):
        if st[i] == st[i - 1]:
            kol += 1
        else:
            kol = 0
        if kol > max:
            max = kol
    return max+1

def maxSymbl(st, mx):
    newKol = 1
    for i in range(1, len(st)):
        if st[i] == st[i-1]:
            newKol += 1
        else:
            newKol = 1
        if newKol == mx:
            return st[i]


def numMaxSymbl(st1, s):
    k = 0
    st1 = st1.replace("", " ")
    newSt = st1.split()
    for i in range(len(newSt)):
        if newSt[i] == s:
            k += 1
    return k

print("Введите список строк")
strings = []
st = input()
myStr = st
while st:
    strings.append(st)
    st = input()
    myStr += st
myStr = sorted(myStr)
myNum = maxNum(myStr)
mySymbl = maxSymbl(myStr, myNum)
numStrings = []
for i in range(len(strings)):
    numStrings.append(numMaxSymbl(strings[i], mySymbl))
otkl = []
sum_otkl = []
for i in range(0, len(strings)):
    sum_otkl.append(pow(myNum-numStrings[i], 2))
    otkl.append(math.sqrt(sum_otkl[i]/(len(strings)-1)))
print(otkl)
i = 0
while i < len(strings)-1:
    if otkl[i] > otkl[i+1]:
        t1 = otkl[i]
        otkl[i] = otkl[i+1]
        otkl[i+1] = t1
        t2 = strings[i]
        strings[i] = strings[i+1]
        strings[i+1] = t2
        i = 0
    else:
        i += 1
print(otkl)
print(strings)

# Задания 15-19. Решить с помощью методов списков.
# Вариант 11. Задачи 11, 23, 35, 47, 59

# 15(11). Дан целочисленный массив, в котором лишь один элемент отличается
# от остальных. Необходимо найти значение этого элемента.

def findElem(ar):
    ar = sorted(ar)
    num = 0
    for i in range(1, len(ar)):
        if ar[i] == ar[i-1]:
            continue
        else:
            num = ar[i]
    return num

print("Введите массив чисел")
arr = []
a = input()
while a:
    arr.append(a)
    a = input()
myElem = findElem(arr)
print(myElem)

# 16(23). Дан целочисленный массив. Необходимо найти два наименьших элемента.

print("Введите массив чисел")
arr = []
a = input()
while a:
    arr.append(a)
    a = input()
arr = sorted(arr)
min1 = arr[0]
min2 = 0
for i in range(len(arr)):
    if min1 != arr[i]:
        min2 = arr[i]
        break
print(min1, min2)