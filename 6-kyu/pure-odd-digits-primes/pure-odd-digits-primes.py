def is_prime(num):
    if num<2:
        return False
    if num==2:
        return True
    if num%2==0:
        return False
    for i in range(3,int(num**0.5)+1,2):
        if num%i==0:
            return False
    return True
def is_pure_odd(num):
    return all(int(d)%2==1 for d in str(num))
​
​
def odd_dig_primes(n): 
    pure_prime=[]
    for i in range(3,n):
        if is_prime(i) and is_pure_odd(i):
            pure_prime.append(i)
    count=len(pure_prime)
    largest_below=pure_prime[-1] if pure_prime else None
    #find smallest above n
    candidates=n+1
    while True:
        if is_prime(candidates) and is_pure_odd(candidates):
            smallest_above=candidates
            break
        candidates+=1
    return [count,largest_below,smallest_above]