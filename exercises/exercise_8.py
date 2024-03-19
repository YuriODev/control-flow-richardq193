# Your solution to Exercise 8
bignum = int(input("Enter a three digit number: "))
num = int(input("Enter a single digit number: "))
bignum_str = str(bignum)
equal = False
for digit in bignum_str:
  if int(digit) == num:
    equal = True
    
if equal:
  print("True")
else:
  print("False")