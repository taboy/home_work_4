#Задайте натуральное число N. Напишите программу, которая составит список простых делителей числа N. (1 - составное число)
n=int(input("vedite csilo"))
a=2
while n>=a:
    if n%a==0:
        print(a)
        n=n/a
    else:a=a+1
