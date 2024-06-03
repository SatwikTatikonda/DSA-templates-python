s1,s2=[],[]

def enque(val):
    s1.append(val)

def dq():

    if not s2:
        while s1:
            s2.append(s1.pop())

    return s2.pop()

for i in range(2,12,2):
    enque(i)

print(dq())
print(dq())
    
    