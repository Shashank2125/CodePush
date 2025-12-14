def to_camel_case(text):
    res=[]
    new_string=list(text)
    i=0
    while i<len(new_string):
        char=new_string[i]
        if char=="-" or char=="_":
            i+=1
            if i<len(new_string):
                res.append(new_string[i].upper())
        else:
            res.append(char)
        i+=1
    return "".join(res)