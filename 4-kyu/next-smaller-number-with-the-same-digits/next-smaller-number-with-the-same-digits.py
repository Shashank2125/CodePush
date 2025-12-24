def next_smaller(n):
    digits=list(str(n))
    #find the pivot
    i=len(digits)-2
    while i>=0 and digits[i]<=digits[i+1]:
        i-=1
    if i<0:
        return -1
    #find right most smallest digit
    j=len(digits)-1
    while digits[j]>=digits[i]:
        j-=1
    #swap digits
    digits[i],digits[j]=digits[j],digits[i]
    digits[i+1:]=reversed(digits[i+1:])
    #leading zero check
    if digits[0]=="0":
        return -1
    return int("".join(digits))
    
    