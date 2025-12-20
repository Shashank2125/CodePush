def expanded_form(num):
    s=str(num)
    n=len(s)
    res=[]
    place=0
    for i in range(n):
        #if string value is not 0
        if s[i]!='0':
            #determine it's place in 7105 then 7000,100....etc
            place=int(s[i])*(10**(n-i-1))
            res.append(str(place))
    return " + ".join(res)
        
        
    pass