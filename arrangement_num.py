print("A program to accept number and generate a list")
list1 = []
list2 = []
print("Enter the numbers, when done press 'end'")
num2 = input("Enter the numbers :    ")
while num2 != "end": 
    num3 = float(num2)
    list1.append(num3)
    num2 = input("Enter the numbers :    ")

#print(list1)
list2 = list1
list2.sort()
print(list2)