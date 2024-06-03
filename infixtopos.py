infix="a+b*(c^d-e)^(f+g*h)-i"
postfix=""
# ans="abcd^e-fgh*+^*+i-"---

def prece(op):
    if op=='^':
        return 4
    elif op=='*' or op=='/':
        return 3
    elif op=='-' or op=='+':
        return 2
    else:
        return 1

s=[]
for i in infix:
    if i.isalpha():
       postfix+=i
    elif i=='(':
        s.append('(')
    elif i==')':

        while s and s[-1]!='(':
            postfix+=s.pop() 
        
        if s[-1]=='(':
            s.pop()
    
    else:

        if not s:
            s.append(i)
        else:

            if prece(i)>prece(s[-1]):
                s.append(i)
            
            else:

                while s and prece(i)<=prece(s[-1]):
                    postfix+=s.pop()
                
                s.append(i)

while s:
    postfix+=s.pop()

print(postfix)
