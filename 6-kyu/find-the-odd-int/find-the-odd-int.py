def find_it(seq):
    mapp={}
    cnt=0
    #add all num and there occurence in mapp
    for num in seq:
        if num in mapp:
            mapp[num]+=1
        else:
            mapp[num]=1
    #Check whether occurence is odd then return nm 
    for num,count in mapp.items():
        if count%2==1:
            return num
    
    return None
            
​