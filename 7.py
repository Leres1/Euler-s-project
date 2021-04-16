# ----------[ 7 ]----------

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.What is the
# 10 001st prime number?

num = 2
i = 1
while num < 10001:
    i += 2
    n = int(i ** 1 / 2)
    if i % 5 == 0:
        i += 2
        n = int(i ** 1 / 2)
    for j in range(3, n + 1):
        if j == n:
            num += 1
            break
        if i % j == 0:
            break
print(i)
# 104759
