import math

def sum_recursive(n, total=0):
    total += n
    if n == 1:
        return total
    left = int(n / 2)
    right = int(math.sqrt(n))
    total = sum_recursive(left, total)
    total = sum_recursive(right, total)
    return total

def testSum_recursive():
    numbers = [1,7,8]
    for n in numbers:
        print(n,':',sum_recursive(n))

testSum_recursive()
