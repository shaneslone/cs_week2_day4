def fibonacciSimpleSum2(n):
    cache = {}
    def fib(n):
        if n == 0: return 0
        if n == 1: return 1
        if n not in cache:
            cache[n] = fib(n-1) + fib(n-2)
        return cache[n]
    cur = 0
    next_fib = 0
    seen = {} 
    while cur < n:
        cur = fib(next_fib)
        seen[cur] = cur
        comp = n - cur
        if comp in seen:
            return True
        next_fib += 1
    return False