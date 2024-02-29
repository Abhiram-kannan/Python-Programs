#Program to convert Decimal number to Binary number

def decimal_to_binary(n):
    return bin(n)[2:]

n = int(input("Enter the decimal number: "))

print("The binary number is: ",decimal_to_binary(n))