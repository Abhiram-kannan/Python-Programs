#Program to find the sum of even natural numbers upto n

def EvenSum(n):
  sum = 0
  for i in range(1,n+1):
    if i%2 == 0:
      sum = sum + i
  return sum

print(EvenSum(10))