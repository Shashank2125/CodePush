def first_non_repeating_letter(s):
    mapp={}
    res=[]
    #store the frequency by storing lowercase alphabets
    for char in s:
        key=char.lower()
        if key in mapp:
            mapp[key]+=1
        else:
            mapp[key]=1
    #if character have == 1 occurence then return the character
    for char in s:
        if mapp[char.lower()]==1:
            return char
    return ""
            
   