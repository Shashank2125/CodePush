def delete_nth(order,max_e):
    mapp={}
    res=[]
    #traverse for nums
    for x in order:
        #increase for occurence with occurence in arr
        mapp[x]=mapp.get(x,0)+1
        #if mapp occurence is not greater than max_occurence
        if mapp[x]<=max_e:
            #append in result
            res.append(x)
    return res
    