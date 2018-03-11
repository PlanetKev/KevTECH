list = ['kev1', 'kev2', 'kev3', 'kev4', 'kev5', 'kev6', 'kev7', 'kev8', 'kev9']
#          0      1        2      3        4      5        6       7      8

print "Number of items in list: " + str(len(list))
first = int(input("The number of the first item of the list: "))
last = int(input("The number of the last number of the list: "))
first -= 1
print list[first:last]


