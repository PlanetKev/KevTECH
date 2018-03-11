def fibo(n):
    if type(n) != int:
        raise TypeError("n must be a positive integer.")
    if n < 0:
        raise ValueError("n must be a positive integer")
    a = 0
    b = 0
    for i in range(0,n):
        temp = a
        a = b + 1
        b = temp + b
    return a


number = input("How many fibonnaci numbers: ")


for i in range(0, number):
    print "\n" + str(fibo(i))
