def division(a,b):
    print(a/b)

def smartDivison(func):

    def inner(a,b):

        if a<b:
            a,b=b,a 
        return func(a,b) 

    # we are not calling iner function but we just return it
    return inner 

newDivision=smartDivison(division)
print(newDivision)
newDivision(2,4)
