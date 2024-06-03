infix="(A–B/C)*(A/K-L)"


# o/p:   "*-A/BC-/AKL"

def prece(op):
    if op=='^':
        return 3
    elif op=='/' or op=='*':
      
        return 2
    elif op=='+' or op=='-':
        return 1
    else:
        return 0

stack=[]
prefix=""
infix=infix[::][::-1]
print(infix)
newinfix=""

for i in range(len(infix)):
    if infix[i]=='(':
       newinfix+=')'
    elif infix[i]==')':
       newinfix+='('
    else:
        newinfix+=infix[i]
print(newinfix)
for i in newinfix:
    print(i)
    if i.isalpha():
        prefix+=i
    elif i=='(':
        stack.append(i)
    elif i==')':
        while stack and stack[-1]!='(':
            prefix+=stack.pop()
        
        if stack and stack[-1]=='(':
            stack.pop()
    
    else:

        if not stack:
            stack.append(i)
        
        if prece(stack[-1])<prece(i):
            stack.append(i)
        elif prece(stack[-1])==prece(i) and stack[-1]=='^':

            while stack and prece(stack[-1])==prece(i) and stack[-1]=='^':
                prefix+=stack.pop()
            stack.append(i)
        elif prece(stack[-1])==prece(i):
            stack.append(i)
        else:

            while stack and prece(stack[-1])>prece(i):
                prefix+=stack.pop()
            stack.append(i)


while stack:
    prefix+=stack.pop()

print(prefix)
print(prefix[::-1])

# infix="(A–B/C)*(A/K-L)"


# # o/p:   "*-A/BC-/AKL"


# infix="(A–B/C)*(A/K-L)"

# def prece(op):
#     if op == '^':
#         return 3
#     elif op == '/' or op == '*':
#         return 2
#     elif op == '+' or op == '-':
#         return 1
#     else:
#         return 0

# stack = []
# prefix = ""
# infix = infix[::-1]

# for i in range(len(infix)):
#     if infix[i] == '(':
#         infix = infix[:i] + ')' + infix[i+1:]
#     elif infix[i] == ')':
#         infix = infix[:i] + '(' + infix[i+1:]

# for i in infix:
#     if i.isalpha():
#         prefix += i
#     elif i == '(':
#         stack.append(i)
#     elif i == ')':
#         while stack and stack[-1] != '(':
#             prefix += stack.pop()
#         if stack and stack[-1] == '(':
#             stack.pop()
#     else:
#         if not stack:
#             stack.append(i)
#         elif prece(stack[-1]) < prece(i) or (prece(stack[-1]) == prece(i) and i != '^'):
#             stack.append(i)
#         else:
#             while stack and (prece(stack[-1]) > prece(i) or (prece(stack[-1]) == prece(i) and i == '^')):
#                 prefix += stack.pop()
#             stack.append(i)

# while stack:
#     prefix += stack.pop()

# print("Infix: ", infix[::-1])
# print("Prefix: ", prefix[::-1])
