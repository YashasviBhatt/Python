from time import sleep
from functools import lru_cache

@lru_cache(maxsize=4)                   # save the cache for previous 4 calls
def func(n):
    sleep(n)
    return 'Hello World'

if __name__ == '__main__':
    print(func(2))
    print(func(4))
    print('The below call won\'t take 2 seconds since the cache for func(2) is saved')
    print(func(2))
    print(func(6))
    print(func(3))
    print(func(9))
    print('The below call won\'t take 9 seconds since the cache for func(9) is saved')
    print(func(9))