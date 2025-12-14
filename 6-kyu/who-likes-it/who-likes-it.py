def likes(names):
    # your code here
    #len of the list/array
    n=len(names)
    #if length=0 then no one likes this
    if n==0:
        return "no one likes this"
    #if length>0 then do all these
    elif n==1:
        return f"{names[0]} likes this"
    elif n==2:
        return f"{names[0]} and {names[1]} like this"
    elif n==3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {n-2} others like this"
    pass