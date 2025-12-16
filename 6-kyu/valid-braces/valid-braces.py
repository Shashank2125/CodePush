def valid_braces(string):
    stack=[]
    for char in string:
        #check for opening braces
        if char=="(" or char=="[" or char=="{":
            #store in stack
            stack.append(char)
        #check for closing braces
        if char==")" or char=="]" or char=="}":
            #if stack is empty return false
            if not stack:
                return False
            #store top most element    
            top=stack.pop()
            #if top most element is not equal to opening brace of char then return false
        if (char==")" and top!="(")or(char=="]" and top!="[")or (char=="}" and top!="{"):
                return False
    #check if stack is completely empty
    return len(stack)==0
                