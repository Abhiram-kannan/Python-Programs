def Decimal_to_binary():
  num = int(input("Enter a decimal number: "))
  binary = bin(num)[2:]
  print("The binary number is: ", binary)

def Binary_to_decimal():
  binary = input("Enter a binary number: ")
  decimal = int(binary, 2)
  print("The decimal number is: ", decimal)

#Menu Driven
while True:
    print("1. Decimal to binary\n2. Binary to decimal\n0. Exit")
    choice = int(input("Enter the choice :"))

    if choice == 1:
      Decimal_to_binary()
      print()
    elif choice == 2:
      Binary_to_decimal()
      print()
    elif choice == 0:
      break
    else:
      print("Invalid choice")
      


