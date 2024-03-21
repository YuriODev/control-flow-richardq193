# Your solution to Exercise 9
num = int(input("Enter a 3 digit number: "))
sum = (num % 10) + (num // 100 % 10)
if sum > num // 10 % 10:
  print(">")
elif sum < num // 10 % 10:
  print("<")
else:
  print("=")