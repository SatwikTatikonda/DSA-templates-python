def Balanced_Parentheses(string):
 
       
    stack =[] 
    close =['}', ']', ')'] 
    dictionary = {'}': '{', ']': '[', ')':'('}
    for parentheses in string:

        if parentheses not in close:

            stack.append(parentheses) 

        else:    

            if not stack or dictionary[parentheses] != stack[-1]: 
                return 0 
            elif dictionary[parentheses] == stack[-1]:
                stack.pop() 
        
            		
    return 0 if stack else 1


string="{[()"
print(Balanced_Parentheses(string))