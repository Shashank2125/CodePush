def max_sequence(arr):
    left=0
    right=0
    max_sum=0
    curr_sum=0
    #move left to right in arr
    while right<len(arr):
        #add current element to sum
        curr_sum+=arr[right]
        #increase the window size
        right+=1
        #if curr_sum is less than 0 
        if curr_sum<0:
            #reset the curr_sum=0
            curr_sum=0
            #reset the window
            left=right
        #check if curr_max is greater than best max we got till now
        max_sum=max(curr_sum,max_sum)
    return max_sum
​