def normalize(x):
    #we check if it is a list
    if isinstance(x,list):
        #if it is a list normalize=[1,[1,2]]=[none,[none,none]]
        return [normalize(e) for e in x]
    #if no list return None
    return None
​
​
def same_structure_as(original,other):
    #check if both are equal after normalization
    return normalize(original)==normalize(other)
    
    