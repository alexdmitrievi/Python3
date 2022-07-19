'''Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части 
элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19'''

n = int(input('введите колличество элементов'))
a = []
for i in range(n):
    new_element = float(input())
    a.append(new_element)

max_d = a[0]%1
min_d = a[0]%1

for i in range(n):
    if a[i]%1>max_d:
        max_d = a[i]%1
    if a[i]%1<min_d:
        min_d = a[i]%1
print(max_d - min_d)








#print(math.modf(3.45 % 1))
