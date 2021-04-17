# ----------[ 10 ]----------

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.Find the sum of all the primes below two million.

n = 2 * 10 ** 6
num = list(range(2, n + 1))
for i in num:
    if i != 0:
        for k in range(2 * i, n + 1, i):
            num[k - 2] = 0
print(sum(list(filter(lambda x: x != 0, num))))
# 142913828922
