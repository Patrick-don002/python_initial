from math import factorial


print("Program to find the factorial of number")
fact = int(input("Enter the number :   "))
total = 1
for i in range (1, fact + 1):
    total *= i

print("The factorial of ", fact, "is    ", total )