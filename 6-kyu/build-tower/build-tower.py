def tower_builder(n_floors):
    #calculate no of stars on each floor
    result=[]
    n=n_floors
    for i in range(n):
        #calculate stars and spaces for adding
        stars=2*i+1
        spaces=n-i-1
        #construct string for required star and spaces
        string=" "*spaces+"*"*stars+" "*spaces
        #append the constructed string
        result.append(string)
        
    return result
        
    # build here