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

# Вариант 11

# Задание 2
# В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один родитель.
# Каждом элементу дерева сопоставляется целое неотрицательное число, называемое высотой.
# У родоначальника высота равна 0, у любого другого элемента высота на 1 больше, чем у его родителя.
# Вам дано генеалогическое древо, определите высоту всех его элементов.
# Программа получает на вход число элементов в генеалогическом древе N. Далее следует N−1 строка,
# задающие родителя для каждого элемента древа, кроме родоначальника. Каждая строка имеет вид имя_потомка имя_родителя.
# Программа должна вывести список всех элементов древа в лексикографическом порядке.
# После вывода имени каждого элемента необходимо вывести его высоту.
# Примечание. Эта задача имеет решение сложности O n( ), но вам достаточно написать решение сложности ( )2 O n
# (не считая сложности обращения к элементам словаря).

def find_heights(N, relations):
    tree = {}
    heights = {}
    for i in range(N-1):
        child, parent = relations[i].split()
        tree[child] = parent
    def find_height(node):
        if node not in heights:
            if node not in tree:
                heights[node] = 0
            else:
                heights[node] = find_height(tree[node]) + 1
        return heights[node]
    for person in sorted(tree.keys()):
        print(person, find_height(person))

N = int(input())
relations = [input() for _ in range(N-1)]
find_heights(N, relations)