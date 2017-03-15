#Problem 4 - Change in My Pocket

change = 0

string = input("Input the string: ").lower()

for x in string:
    if x == "p":
        change += .01
    elif x == "n":
        change += .05
    elif x == "d":
        change += .10
    elif x == "q":
        change += .25


check = 0
change = round(change, 2)

for x in str(change):
    check += 1
if check == 3:
    change = str(change) + "0"

print("The value of the change is: $" + str(change))