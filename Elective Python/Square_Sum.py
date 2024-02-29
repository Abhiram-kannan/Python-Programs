#Program to find the sum of the squares of n natural numbers

def Squaresum(n):
  sum = 0
  for i in range(1,n+1):
    sum = sum + i**2
  return sum

print(Squaresum(10))