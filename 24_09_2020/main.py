#! /usr/bin/env python3

import my_lib

print("Случайное число в диапазоне от {} до {}: {}".format(5, 8, my_lib.get_int_random(5, 8)))

simple_array = [0, 2, 8, 2, 3, 1, 9]
print("Длинна массива {} равна: {}".format(simple_array, my_lib.get_length_array(simple_array)))