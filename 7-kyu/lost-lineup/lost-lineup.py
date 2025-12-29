def find_lineup(distances):
    n=len(distances)
    res=[-1]*n
    for i in range(n):
        pos=distances[i]
        #postion must be valid
        if pos<0 or pos>=n:
            return []
        #if position is already taken Impossible
        if res[pos]!=-1:
            return []
        #place the person at thier postion
        res[pos]=i+1
    return res
    pass