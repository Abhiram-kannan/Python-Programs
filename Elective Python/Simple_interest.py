#To calculate simple interest we need three parameters
#principal amount, rate of interest, and time

def simple_interest(principal, rate, time):
    return principal * rate * time / 100

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest(in %): "))
time = float(input("Enter the time(in years): "))
print("The simple interest is: ",simple_interest(principal,rate,time))