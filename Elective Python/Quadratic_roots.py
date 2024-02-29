#To find the roots of a quadratic equation

import math
a = int(input("Enter coefficient of x^2: "))
b = int(input("Enter coefficient of x: "))
c = int(input("Enter constant value: "))

print("The polynomial is ", a,"x^2 + ",b,"x + ",c, sep = "")
discriminant = b**2 - 4 * a * c

if discriminant > 0:
  root1 = ( -b + math.sqrt(discriminant)) / (2 * a) 
  root2 = ( -b - math.sqrt(discriminant)) / (2 * a) 
  print("The roots of the quadratic polynomial are ",root1,"and",root2)
if discriminant == 0:
  root = -b / (2 * a)
  print("The roots of the quadratic polynomial are ",root)
else:
  real = -b / (2 * a)
  imaginary = math.sqrt(abs(discriminant)) / (2 * a)
  print( real + imaginary* 1j, real - imaginary* 1j,) 
  #ij represents complex number, that is sqrt(-1)

