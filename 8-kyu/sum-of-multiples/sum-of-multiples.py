def sum_mul(n, m):
    if n<=0 or m<=0:
        return "INVALID"
    total=0
    for i in range(n,m,n):
        total+=i
    return total
        
    pass