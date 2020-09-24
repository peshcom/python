import random

# Получение целого числа в диапазоне от a до b
def get_int_random(a, b):
	return random.randint(a, b)

def get_length_array(array=None):
	return array.__len__()