import time
import matplotlib.pyplot as plt
# Time module is used to time how long computations of the prime range take and also to sleep
print "KevTECH Simple Prime Number Analyser"
print "------------------------------------\n"
# Actual Prime True or False Function


def isitPrime(n):
    if n == 1:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    else:
        return True
# List and Variable Declaration
list = []
primes = []
composite = []
x = int(input("Lower boundary(greater than or equal to 1): "))
n1 = int(input("Upper Boundary(greater than lower boundary): "))
s = int(input("Step(If you don't want a step enter 1): "))
# Exceptions
if x < 1:
    print("Please enter number greater than or equal to one")
elif n1 < x:
    print("Please enter an upper boundary that is greater than the lower boundary")
elif s < 1:
    print("Please enter a step that is greater than or equal to 1")
elif s > n1:
    print("Please enter a step that is less than the upper boundary")
else:
    n1 += 1
    print("True means that it is a Prime number and False means that it is a Composite number")
# Used to Time how long it takes to find primes in the user given range
    t0 = time.time()
    for i in range(x, n1, s):
        print(i, str(isitPrime(i)))
        list.append(isitPrime(i))
        if isitPrime(i) == True:
            primes.append(i)
        elif isitPrime(i) == False:
            composite.append(i)
    t1 = time.time()
    print("Task completed in: " + str(t1 - t0) + " seconds")
# Analysis
    print "\nIn digits " + str(x) + " through " + str(n1 - 1) + " with a step of " + str(s) + " there are " + str(list.count(True)) + \
          " prime numbers and " + str(list.count(False)) + " composite numbers"
    if (n1 - 1) >= 5:
        print "\nThere are " + str((list[0:5]).count(True)) + " primes in the first 5 digits"
        print "There are " + str((list[-5:]).count(True)) + " primes in the last 5 digits"
    if (n1 - 1) >= 10:
        print "\nThere are " + str((list[0:10]).count(True)) + " primes in the first 10 digits"
        print "There are " + str((list[-10:]).count(True)) + " primes in the last 10 digits"

    if (n1 - 1) >= 100:
        print "\nThere are " + str((list[0:100]).count(True)) + " primes in the first 100 digits"
        print "There are " + str((list[-100:]).count(True)) + " primes in the last 100 digits"
    if (n1 - 1) >= 1000:
        print "\nThere are " + str((list[0:1000]).count(True)) + " primes in the first 1000 digits"
        print "There are " + str((list[-1000:]).count(True)) + " primes in the last 1000 digits"
    kev = int(input("\nUser First and Last amount : "))
    if (n1 - 1) >= kev:
        print "\nThere are " + str((list[0:kev]).count(True)) + " primes in the first " + str(kev) + " digits"
        print "There are " + str((list[-kev:]).count(True)) + " primes in the last " + str(kev) + " digits"
    time.sleep(0.5)
    print("\nComputing addition analysis and data...")
    time.sleep(0.5)
    try:
        print "\nFirst composite found: " + str(composite[0])
        print "Last composite found: " + str(composite[-1])
        print "All composites found in range: " + str(composite)
        print "\nAll primes found in range: " + str(primes)
        print "\nFirst prime found : " + str(primes[0])
        print "Last prime found: " + str(primes[-1])

    except IndexError:
        print "There are no primes in this range"
    nprime = int(input("\nFind the 'nth' prime of all primes found in the user given range. What is n? "))
    if nprime > len(primes):
        print "Nth primes is out of range of the list of primes"
    else:
        nprime -= 1
        print "Nth prime number =", primes[nprime]

# Basic Text-Based Graphical Representation
    print ""
    print "In this basic graphical display, 'X' represents prime numbers and '.' represents composite numbers in the user provided range: \n"
    for k in range(x, n1, s):
        if isitPrime(k) == True:
            print "X",
        else:
            print ".",
    print("\n")
    print("\n")
    print("Computing a line graph and scatter plot of the data, as well as a bar graph of primes to composites...")
    time.sleep(1)
# Graphs of data
    list1 = range(x, n1, s)
    list2 = []
    primelist = []
    compositelist = []
    for i in range(x, n1, s):
        if isitPrime(i) == True:
            list2.append(int("1"))
            primelist.append(int("1"))
        else:
            list2.append(float("0"))
            compositelist.append(int("0"))
    colorlist = []
    for i in list2:
        if i == 0:
            colorlist.append('red')
        elif i == 1:
            colorlist.append('blue')
        else:
            colorlist.append('green')
    print "x values: " + str(list1)
    print "y values: " + str(list2)
    print "If the y is 1 the number is prime and if it is 0 the number is composite"
    # Scatter Plot
    plt.scatter(list1, list2, color=colorlist, marker=".", s=7, alpha=0.9)
    plt.xlabel("User Given Digits")
    plt.ylabel("Composites(0) and Primes(1)")
    plt.yticks([0, 1])
    plt.title("Scatter Plot of the Frequency of Primes and Composites")
    plt.show()
    # Line Graph
    plt.plot(list1, list2)
    plt.xlabel("User Given Digits")
    plt.ylabel("Composites(0) and Primes(1)")
    plt.yticks([-1, 0, 1, 2])
    plt.title("Line Plot of the Frequency of Primes and Composites")
    plt.grid()
    plt.show()
    # Bar Graph
    plt.bar(1, len(primelist), color='r')
    plt.bar(2, len(compositelist))
    plt.bar(3, len(primelist+compositelist), color='g')
    plt.xlabel("Primes(Red), Composites(Blue), and All(Green)")
    plt.ylabel("Number of Prime and Composite Digits")
    plt.title("Bar Graph of Primes vs Composites")
    plt.show()
    # Histogram
    plt.hist(list2)
    plt.xlabel("Composites(0) and Primes(0)")
    plt.ylabel("Number of Prime and Composite Digits")
    plt.title("Histogram of the number of Prime and Composite Digits")
    plt.show()
    print("\nThank you for using KevTECH")
