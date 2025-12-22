def perimeter(n):
    # your code
    if n==0:
        return 4
    a,b=1,1
    #generates first fibbonacci
    total=a+b
    #generate remaining fibonacci
    for _ in range(2,n+1):
        a,b=b,a+b
        total+=b
    #returns area by side * perimeter
    return 4*total