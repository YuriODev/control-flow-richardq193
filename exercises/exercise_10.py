# Your solution to Exercise 10
d1 = int(input(""))
d2 = int(input(""))
d3 = int(input(""))
d4 = int(input(""))
d5 = int(input(""))
d6 = int(input(""))
right = False
count = 0
if d1 == 1:
  count = count + 1
if d2 == 1:
  count = count + 1
if d3 == 1:
  count = count + 1
if d4 == 4:
  count = count + 1
if d5 == 4:
  count = count + 1
if d6 == 1:
  count = count + 1
if count == 6:
  print("Yes")
else:
  print("No")