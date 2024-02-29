def swap(a,b):
  a,b = b,a
  return a,b

a = int(input("Enter num1: "))
b = int(input("Enter num2: "))
print("Before swap: ",a,b)
print("After swap: ",swap(a,b))