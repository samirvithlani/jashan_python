

def safeDiv(func):
    
    def inner(x,y):
        #func(x,y)
        if(y==0):
            print("can not divide by zero..")
        else:
            func(x,y)    

    return inner

@safeDiv
def div(a,b):
    print("div",a/b)


div(100,0)    
    
