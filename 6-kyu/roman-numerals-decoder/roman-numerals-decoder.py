def solution(roman : str) -> int:
    """complete the solution by transforming the roman numeral into an integer"""
    #store every roman plus it's value in the map
    mapp={
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    total=0
    for i in range(len(roman)-1):
        #roman i is smaller than i+1 then negate else add value to total
        if mapp[roman[i]]<mapp[roman[i+1]]:
            total-=mapp[roman[i]]
        else:
            total+=mapp[roman[i]]
    #add first character
    total+=mapp[roman[-1]]
    return total