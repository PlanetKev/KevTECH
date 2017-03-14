#Problem 2 - Pythagorean Triple


def check(a, b, c):
    asquared = a*a
    bsquared = b*b
    csquared = c*c
    if asquared + bsquared == csquared and 0 < a < b < c:
        print("A Pythagorean Triple")
    else:
        print("Not a Pythagorean Triple")


vara = int(input("Enter a: "))
varb = int(input("Enter b: "))
varc = int(input("Enter c: "))

check(vara, varb, varc)
