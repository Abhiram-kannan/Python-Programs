#program to convert binary number to decimal number

def Bin_to_decimal(num):
  decimal = 0
  for i in range(len(num)):
    decimal += int(num[i]) * 2**(len(num) -i -1)
  return decimal

#To read a binary number
num = input("Enter a binary  number: ")
print(Bin_to_decimal(num))