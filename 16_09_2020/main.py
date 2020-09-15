#! /usr/bin/env python3


# Переменные
a = 10				# int
b = 3.1415926		# float
c = "Hello"			# string
d = [1, 2, 3]		# array


# ввод вывод
my_str = input("Введите строку: ")
print("Вы ввели строку: " + my_str)

a = int(input("Введите значение А: "))
print("Вы ввели число: " + str(a))

# Ветвление
if a % 2:
	print("Это не четное число")
else:
	print("Это четное число")

print("Вывод чисел:")
print(a)
print("Это A", a)
print(f"Это A {a}")
print("Это А {}".format(a))
print("Это число А: " + str(a) + "!")


print("--------- for -----------")
for i in range(0, 5): # от 0 до 4
	print(i)

print("--------- for arr -----------")
a = [1, 5, 2, 55, 22]
for i in a:
	print(i)

print("-------- While ----------")

a = 0
while a < 4: # Вывод чисел от 0 до 4
	print(a)
	a = a + 1


print("------- Функции ---------")


def my_simple_func_sum(a, b):
	# Функция подсчета суммы двух чисел
	c = a + b
	return c

print(my_simple_func_sum(11, 2))

print("-------- Разбор строки на символы --------")
my_str = input("Введите строку: ")
print("Вы ввели строку: " + my_str)
for i in my_str:
	print(i)