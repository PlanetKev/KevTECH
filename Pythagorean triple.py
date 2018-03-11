def check(a, b, c):
    if a + b == c and 0 < a < b < c:
        print "Pythagorean Triple Detected"
    else:
        print "Pythagorean Triple not Detected"
print("KevTECH Pythagorean Triple Detector")
while 1 == 1:
    asquared = float(input("a= ")) ** 2
    bsquared = float(input("b= ")) ** 2
    csquared = float(input("c= ")) ** 2
    check(asquared, bsquared, csquared)
