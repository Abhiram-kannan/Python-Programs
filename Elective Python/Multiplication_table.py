def Multi(num, upto):
  for i in range(1, upto+1):
    print(num,"x",i,"=",num*i)

num = int(input("Enter the number: "))
upto = int(input("Enter the number upto which multiplication table is to be displayed: "))
Multi(num, upto)