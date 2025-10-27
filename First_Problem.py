#Problem 01: Write a Python program to sum all the items in a list.

def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

myList = [1,2,3,4,5]
result = sum_of_list(myList)
print("The sum of the list is:", result)