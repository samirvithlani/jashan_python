

def safeDiv(func):
    
    def inner(x,y):
        #func(x,y)
        if(y==0):
            print("can not divide by zero..")
            return None
        else:
           return func(x,y)    

    return inner

@safeDiv
def div(a,b):
    return a/b


x = div(100,2)    
print(x)
    
