# Your solution to Exercise 12
num = int(input("Enter a number: "))
num = list(str(num))
for i in range (4):
  if num[i] == "2" or num == "4" or num == "6" or num == "8" or num == "0":
    num[i] = "*"
print(num)