print("A program to find numbers that are divisible by 7 but not a multiple of 5")
print("User interactive aspect")
var3 = int(input("Enter the starting number :    "))
var4 = int(input("Enter the stopping number :   "))
counter = int(0)
for num in range (var3, var4 + 1):
    if num % 7 == 0:
        if num % 5 != 0:
            print(num , "divisible by 7 but not a multiple of 5")
            counter += 1

print("The total number counted is   ", counter)