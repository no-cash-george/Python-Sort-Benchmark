import random 
import time

start = time.time()
A = []

for i in range(0,1000000):
    A.append(random.randrange(0,1000000))

A.sort()
end = time.time()

print(end - start)
