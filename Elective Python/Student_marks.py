class Student:
  def __init__(self, name, rollno, mark1, mark2, mark3):
    self.name = name
    self.rollno = rollno
    self.mark1 = mark1
    self.mark2 = mark2
    self.mark3 = mark3
  
  def average(self):
    self.total = (self.mark1 + self.mark2 + self.mark3) / 3
    print("Total percentage is :", self.total)
  
  def result(self):
    if self.total > 50:
      print("Pass")
      print("Grade is: ",end = " ")
      if self.total >= 90:
        print("Excellent")
      elif 80 < self.total < 90:
        print("Good")
      elif 70 < self.total <= 80:
        print("Satisfactory")
      elif 50 < self.total <= 70:
        print("Poor")
    else:
      print("Failed")
n = input("Enter the name of the student: ")
roll = int(input("Enter the roll no: "))
m1 = int(input("Enter the mark1: "))
m2 = int(input("Enter the mark2: "))
m3 = int(input("Enter the mark3: "))

s1 = Student(n,roll,m1,m2,m3)
s1.average()
s1.result()

