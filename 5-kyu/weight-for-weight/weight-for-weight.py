def weight_key(num_str):
    return(sum(map(int,num_str)),num_str)
#this function ex->"100"=1,0,0=1+0+0=1 so it returns (1,100)
#converts every character into int and map element
​
def order_weight(strng):
    # your code
    #handle widespaces
    if not strng.strip():
        return ""
    #handles extra spaces in between 100 20 90 ->100,20,90
    nums=strng.split()
    #sort nums according to wieght key
    nums.sort(key=weight_key)
    #returns in order
    return " ".join(nums)
        