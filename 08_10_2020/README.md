Третья часть
---

Чтение/запись в файл
---
Чтение из файла
```python
f = open("filename", 'r')
a = f.read()
print(a) # Выведет все содержимое файла

a = f.readline()
print(a) # Выведет первую строку

a = f.readline()
print(a) # Выведет вторую строку


f.close() # Закрываем файл после всей работы
```

Запись
```python
f = open('1', 'w')
f.write("text")
f.close()
```


Генератор псевдослучайных чисел:
---
```python
import random
a = random.randint(A, B) # Случайное число x из диапазона [A; B]
print(a)
```