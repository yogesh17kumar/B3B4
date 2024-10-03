import time



n = 100000

def wrapper(func, *args, **kwargs):
    def wrapped(*args, **kwargs):

        start_time = time.time() * 1000000
        func(*args, **kwargs)
        end_time = time.time() * 1000000
        print(f"\n n={n} Time to execute is {end_time - start_time} micro seconds\n")

    return wrapped
@wrapper
def count(n):
    for i in range(0, n):
        a = n * 10

count(n)

@wrapper
def random():
    pass

random()
    

#wrapped_function = wrapper(count,n)
#wrapped_count = wrapper(count, n)
#wrapped_count(n)

