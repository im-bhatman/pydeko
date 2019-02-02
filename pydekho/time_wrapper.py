import time

def time_wrapper(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print("Time taken to execute :: ",time.time()-start)
        return res
    return wrapper