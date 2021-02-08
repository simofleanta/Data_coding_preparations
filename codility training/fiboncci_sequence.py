#memoization to cache values 
#use fib cache with {}
fibonacci_cache={}


def fibonacci (n):
    """if I have cached a value then return the value"""
    if n in fibonacci_cache:
        return fibonacci_cache[n]
# perform the nth tem if cluase    
    if n==1:
        value=1
    elif n== 2:
        value=2
    elif n>2:
        value=fibonacci(n-1)+fibonacci(n-2)
# cache the value and return it 
    fibonacci_cache[n]=value
    return value

for n in range(1,101):
    print(n, ":", fibonacci(n))

