def fib(n):
    """Calculates the nth Fibonacci number"""
    def fib_pair(k):
        if k==0:
            return (0,1)
        a,b=fib_pair(k//2)
        c=a*((b<<1)-a)
        d=a*a+b*b
        if k&1:
            return (d,c+d)
        else:
            return (c,d)
    if n==0:
        return 0
    if n<0:
        f=fib_pair(-n)[0]
        return -f if n%2==0 else f
    return fib_pair(n)[0]