def hamming(n):
    h=[0]*n
    h[0]=1
    i2=i3=i5=0
    for i in range(1,n):
        next2=h[i2]*2
        next3=h[i3]*3
        next5=h[i5]*5
        h[i]=min(next2,next3,next5)
        if h[i]==next2:
            i2+=1
        if h[i]==next3:
            i3+=1
        if h[i]==next5:
            i5+=1
    return h[n-1]