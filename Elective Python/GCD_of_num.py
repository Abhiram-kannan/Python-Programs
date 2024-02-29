#program to find the gcd of a number

def gcd(a,b):
  if b == 0:
    return a
  else:
    return gcd(b,a%b)
  
a = int(input("Enter num1: "))
b = int(input("Enter num2: "))

print("GCD of",a,"and",b,"is",gcd(a,b))

