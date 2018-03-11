import time
print "Simple Prime Number Analyser \n"
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

# Analysis

if x < 1:
    print("Please enter number greater than or equal to one")
elif n1 < x:
    print("Please enter an upper boundary that is greater than the lower boundary")
else:
    n1 += 1
    print("True means that it is a Prime number and False means that it is a Composite number")
    for i in range(x, n1):
        print(i, str(isitPrime(i)))
        list.append(isitPrime(i))
        if isitPrime(i) == True:
            primes.append(i)
        elif isitPrime(i) == False:
            composite.append(i)
    print "\nIn numbers " + str(x) + " through " + str(n1 - 1) + " there are " + str(list.count(True)) + \
          " prime numbers and " + str(list.count(False)) + " composite numbers"
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

    print("Computing addition analysis and data...")
    time.sleep(3)
    print "\nAll primes found in range: " + str(primes)
    print "All composites found in range: " + str(composite)
    print "\nFirst prime found : " + str(primes[0])
    print "Last prime found: " + str(primes[-1])
    print "\nFirst composite found: " + str(composite[0])
    print "Last composite found: " + str(composite[-1])
    numberkev = int(input(("Choose specific number to see if it is prime or composite: ")))
    if isitPrime(numberkev) == True:
        print str(numberkev) + " is Prime"
    else:
        print str(numberkev) + " is Composite"





