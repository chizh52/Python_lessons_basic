
__author__ = 'Степаненко Виктор Владимирович'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

a=input('Введите целое число:')
i=0
while i < len(a):
      print(a[i])
      i +=1

a=input('Введите целое число:')
for i in a:
      print(i)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

a=input('Введите переменную 1:')
b=input('Введите переменную 2:')
c=a
a=b
b=c
print('Переменная 1='+a)
print('Переменная 2='+b)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

a=int(input('Скока тебе лет, чувак? '))
if a>=18 :
        print('Покажи паспорт и наливай')
else:
        print('Домой, баиньки')
