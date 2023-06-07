#This is list and is initially  by using [] and data is seperated by ","
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
           
# Explaining how list works
# List can hold multiple data types and uses indexing to get specific data every list
# All list indexes start from 0 

# If we wanna get the number 1 from the list we must direct it to its specific index, in this casw index 0
one = numbers[0]

two = numbers[1]


print(f"\nThe number at index 0 is number: {one}\n")

print(f"\nThe number at index 1 is number: {two}\n")


# Different types of for loops

# Getting the numbers based on the size of the list (number of items within the list)
for number in range(len(numbers)):
    
    print(f"\nThe current index is: {number} and The current number is: {numbers[number]}\n")

# Getting the numbers diretly within the list
for number in numbers:
     print(f"\nThe current index is: {number} and The current number is: {numbers[number]}\n")