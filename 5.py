# ----------[ 5 ]----------

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible  (divisible with no remainder) by all of the numbers
# from 1 to 20?

stat = False
i = 0
while True:
    if stat:
        break
    i += 20
    for j in range(1, 21):
        if i % j != 0:
            break
        if j == 20:
            stat = True
            print(i)
            break
# 232792560
