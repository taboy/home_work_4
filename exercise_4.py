#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и вывести на экран.
# 33. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

# k = (int(input( k = ")))
list1=[]
k = 3
for i in range (k,0,-1):
    c = random.randint(0,100)
    a=(f'{c}x^{i} + ')
    list1.append(a)

b=(f'{random.randint(0,100)} = 0\n')
list1.append(b)
listToStr = ' '.join([str(elem) for elem in list1])
print(listToStr)


