def SortList(List, n):
  for i in range(n):
    for j in range(n - 1):
      if List[j] > List[j+1]:
        List[j],List[j+1] = List[j+1],List[j]
  return List


List = []
n = int(input("Enter the number of items in the list: "))
for i in range(n):
  item = int(input("Enter item: "))
  List.append(item)

print(SortList(List, n))
