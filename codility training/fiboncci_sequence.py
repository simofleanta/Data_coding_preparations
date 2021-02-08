
fibonacci={}

def fibonacci_cache(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    
    if n==1:
        value=1
    elif n== 2:
        value=2
    elif n>2:
        value=fibonacci(n-1)+fibonacci(n-2)
    # cache
    fibonacci_cache[n]=value
    return value

for n in range(1,101):
    print(n, ":", fibonacci(n))

    