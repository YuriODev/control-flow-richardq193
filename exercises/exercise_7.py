# Your solution to Exercise 7
a = float(input("Enter a number: "))
b = float(input("Enter another number: "))
op= input("Enter an operation: ")
result = ""
if op == "+" :
  result = a + b
elif op == "-":
  result = a - b
elif op == "*":
  result = a * b
elif op == "%":
  result = a % b
elif op == "//":
  if b == 0:
    result = "Division by 0!"
  else:
    result = a // b
elif op == "pow":
  result = a**b
print(result)