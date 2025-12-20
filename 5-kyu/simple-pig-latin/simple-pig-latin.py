def pig_it(text):
    res=[]
    for word in text.split():
        #isalpha checks for char is to be alphabet
        if word.isalpha():
            #append result from word[1] then at last the first word with ay
            res.append(word[1:]+word[0]+"ay")
        else:
            res.append(word)
    return " ".join(res)
    #your code here