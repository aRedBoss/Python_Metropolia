import random

N = 10000
n = 0

toistut = 0

while toistut < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x ** 2 + y ** 2 < 1:
        n += 1

    toistut += 1

pii = 4 * n / N
print (pii)