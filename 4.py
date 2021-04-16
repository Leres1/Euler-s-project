# ----------[ 4 ]----------
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
# is 9009 = 91 х 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers

stat = False
i = 999 * 999
while i > 0:
    if stat:
        break
    num = str(i)
    if num[::1] == num[::-1]:
        j = 100
        while j < 999:
            if i % j == 0:
                if len(str(int(i / j))) == 3:
                    print("%s * %s = %s" % (j, int(i / j), i))
                    stat = True
                    break
            j += 1
    i -= 1
# 913 * 993 = 906609
