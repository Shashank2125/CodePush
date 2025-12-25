def sum_for_list(lst):
    from collections import defaultdict
    #for finding distinct prime factors for n
    def prime_fact(n):
        #no duplicate primes
        factors=set()
        #smallest Prime=2
        d=2
        #loop until n sqaure root
        while d*d<=n:
            #if d divides n remove all occurence of prime 
            while n%d==0:
                #add it to the set
                factors.add(d)
                #remove factor of d from n
                n//=d
            #handle next divisor
            d+=1
        #remaining prime
        if n>1:
            factors.add(n)
        return factors
    prime_sum=defaultdict(int)
    for num in lst:
        for p in prime_fact(abs(num)):
            prime_sum[p]+=num
    return [[p , prime_sum[p]] for p in sorted(prime_sum)]