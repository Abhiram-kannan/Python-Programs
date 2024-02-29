def readMatrix(rows, cols):
  matrix = []
  print("Enter the elements of the matrix")
  for i in range(rows):
    row = []
    for j in range(cols):
      item = int(input("Enter the number: "))
      row.append(item)
    print()
    matrix.append(row)
  return matrix

def addMatrix(m1, m2):
  if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
    print("Matrix dimensions are not the same")
    return None
  m3 = []
  for i in range (len(m1)):
    row = []
    for j in range(len(m1[0])):
      row.append(m1[i][j] + m2[i][j])
      m3.append(row)
      print()
  return m3

def subMatrix(m1, m2):
  if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
    print("Matrix dimensions are not the same")
    return None
  m3 = []
  for i in range (len(m1)):
    row = []
    for j in range(len(m1[0])):
      row.append(m1[i][j] - m2[i][j])
      m3.append(row)
      print()
  return m3

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
m1 = readMatrix(rows, cols)
m2 = readMatrix(rows, cols)
print(addMatrix(m1, m2))
print(subMatrix(m1, m2))