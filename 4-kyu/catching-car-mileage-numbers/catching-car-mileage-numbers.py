def is_interesting(number, awesome_phrases):
    def is_interesting_num(n):
        #number is less than 100
        if n<100:
            return False
        s=str(n)
        #Any digit follow by all zeroes
        if s[0]!='0' and set(s[1:])=={'0'}:
            return True
        #All digits the same
        if len(set(s))==1:
            return True
        #digits are increment order
        inc="1234567890"
        if s in inc:
            return True
        #digits are decrement order
        dec="9876543210"
        if s in dec:
            return True
        #palindrome
        if s==s[::-1]:
            return True
        #Awesome Pharase
        if n in awesome_phrases:
            return True
        return False
    #Check current and next two number
    if is_interesting_num(number):
        return 2
    if is_interesting_num(number+1) or is_interesting_num(number+2):
        return 1
    return 0
        
            