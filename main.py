import time

def count(n):
    for i in range(0, n):
        a = n * 10

ns = [10000, 234324, 34567, 345, 344, 342]

for n in ns:
    start_time = time.time() * 1000000
    count(n)
    end_time = time.time() * 1000000
    print(f"Time to execute for n={n} is {end_time - start_time} micro seconds")