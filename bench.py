import random 
import time

n = int(input("How many passes do you want me to perform? : \n"))
start = time.time()
A = []
for j in range(0,n):
    print("Pass",j)
    for i in range(0,1000000):
        A.append(random.randrange(0,1000000))

    A.sort()
    A = []
end = time.time()

print(end - start)
