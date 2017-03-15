
numbers = []
# creating the list for sorting


# sort the array and print -
def sort(array):
    array.sort()
    print("Ordered Sequence: " + str(array))
num = int(input("Enter the length of the sequence: "))
# input length of the sequence

while num > 0:
    add = int(input("Number: "))
    numbers.append(add)
    num -= 1

sort(numbers)

