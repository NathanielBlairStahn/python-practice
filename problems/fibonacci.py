def fibonacci_generator(num_terms=float('inf'), upper_bound=float('inf')):
    """Generates Fibonacci numbers."""
    previous=1
    current=0
    for _ in range(num_terms):
        if current > upper_bound:
            break

        yield current
        next = previous+current
        previous = current
        current = next

def even_fibonacci_generator(num_terms=float('inf'), upper_bound=float('inf')):
    """Generates even Fibonacci numbers"""
    fib_gen = fibonacci_generator(3*num_terms,upper_bound)
    while True:
        try:
            yield next(fib_gen)
            next(fib_gen)
            next(fib_gen)
        except StopIteration:
            break

def forward_difference(arr,h=1,order=1):
    """Returns the forward differences of an array.
    h = increment
    order = number of times to apply forward differnce operator
    """
    diffs = arr
    for _ in range(order):
        diffs = [diffs[i+h] - diffs[i] for i in range(len(diffs)-h)]
    return diffs
