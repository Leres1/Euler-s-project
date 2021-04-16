# ----------[ 9 ]----------

# A Pythagorean triplet is a set of three natural numbers, a <b < c, for which, a^2 + b^2 = c^2. For example,
# 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

a = 0
b = 0
c = 1000
while True:
    if a ** 2 + b ** 2 == c ** 2:
        print("a - %s b - %s c - %s" % (a, b, c))
        break
    if b > a:
        a += 1
        c -= 1
    else:
        b += 1
        c += a - 2
        a = 1
# a - 200 b - 375 c - 425
