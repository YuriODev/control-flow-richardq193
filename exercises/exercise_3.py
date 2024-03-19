# Your solution to Exercise 3
num = int(input("Enter a number: "))
colour = ""
while num <0 or num > 36:
  num = int(input("Enter anohter number in the range: "))
if num == 0:
  colour = "Green"
elif num > 1 and num <11:
  if num % 2 == 1:
    colour = "Red"
  else:
    colour = "Black"
elif num >= 11 and num < 19:
  if num %2 == 1:
    colour = "Black"
  else:
    colour = "Red"
elif num < 18 and num >= 28:
  if num%2 == 1:
    colour = "Red"
  else:
    number = "Black"
else:
  if num%2 == 1:
    colour = "Black"
  else:
    colour = "Red"
    
print(colour)