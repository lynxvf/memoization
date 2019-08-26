def memoize(func):
    cache_dict = {}

    def inner(*args):
        if args in cache_dict:
            return cache_dict[args]
        else:
            cache_dict[args] = func(*args)
            return cache_dict[args]

    return inner


@memoize
def fibonacci(number):
    if number < 2:
        return number
    return fibonacci(number-1) + fibonacci(number-2)


if __name__ == "__main__":
    print([fibonacci(number) for number in range(1000)])

