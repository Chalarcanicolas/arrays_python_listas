import random

x = [None] * 10

for i in range(10):
    x[i] = random.uniform(0, 1)

for i in range(10):
    print(x[i])
