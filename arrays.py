"""This program will do some array manipuations calcaultions
Emily Maher January 27, 2025"""

import numpy as np
first = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
second = np.array([-0.5, -2.5, 3.1, 2.0, 1.0])
print(first,second)

dot = np.dot(first,second)
print(dot)

first[2] = -2.0
second[1]=1.0
print(first,second)

third = first + second
print(third)

dot = np.dot(first,second)
print(dot)

a = np.zeros(3)
print(a)

b = np.ones((2,3))
print(b)
