
import numpy as np
import math

a = eval(input("Please Enter a Number: "))
b = eval(input("Please Enter a Number: "))

sum = a + b
difference = a - b
product = a*b
quotient = a/b
power = pow(a,b)
sin_value = np.sin(a)
cos_value = np.cos(b)
sin_value_deg = np.sin(np.deg2rad(a))
cos_value_deg = np.cos(math.radians(b))

print("The sum of your numbers is", "{:.1f}".format(sum))
print("The difference of your numbers is", "{:.2f}".format(difference))
print("The product of your numbers is", "{:.4f}".format(product))
print("The quotient of your numbers is", "{:.5f}".format(quotient))
print("The power of your numbers is", "{:.6f}".format(power))
print("If your number was in radians, the sin of your first numbers in is", "{:.3f}".format(sin_value))
print("If your number was in radians, the cos of your first numbers in is", "{:.3f}".format(cos_value))
print("If your number was in degrees, the sin of your first numbers in is", "{:.3f}".format(sin_value_deg))
print("If your number was in degrees, the cos of your first numbers in is", "{:.3f}".format(cos_value_deg))

