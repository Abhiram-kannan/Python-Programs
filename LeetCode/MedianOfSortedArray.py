
def inputArray():
   n = int(input("Enter the number of elements: "))
   arr = []
   for i in range(n):
      arr.append(int(input("Enter the element: ")))
   return arr
def Solution():
  num1 = inputArray()
  num2 = inputArray()
  new = num1 + num2
  new.sort()
  print(new)
  #for median
  mid = len(new) // 2
  if len(new) % 2 == 0:
    return (new[mid - 1] + new[mid]) / 2
  else:
    return new[mid]

print(Solution())


