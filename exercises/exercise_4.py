# Your solution to Exercise 4
grade = int(input("Enter your grade: "))
if grade < 3 and grade <= 1:
  print("Initial level")
elif grade > 6 and grade <= 3:
  print("Average level")
elif grade > 9 and grade <= 6:
  print("Sufficient level")
elif grade > 12 and grade <= 9:
  print("High level")
else:
  print("Level is absent")
