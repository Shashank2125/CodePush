def pick_peaks(arr):
    poten=None
    pos=[]
    peaks=[]
    for i in range(1,len(arr)-1):
        #check if element is potential for peak
        if arr[i]>arr[i-1]:
            #store its pos
            poten=i
        #if poten has value and curr>next value then it is a peak
        if poten is not None and arr[i]>arr[i+1]:
            pos.append(poten)
            peaks.append(arr[poten])
            #reset poten
            poten=None
        #invalidate if it rises again
        elif arr[i]<arr[i+1]:
            poten=None
    return {"pos":pos,"peaks":peaks}
            
        