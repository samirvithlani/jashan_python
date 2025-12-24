#decoratoes are pure pyrhon function which wull accetp a1 function as param and will return inner function object
#use of decorator is to hcange behaviour of funciton without changing code..
persons = 100
def order_food(func): #3 func == throw_party
    
    def inner(): #6
        
        #func() #8 
        if(persons>100):
            print("ordering food...") #7
            func()
        else:
            print("no party")    

    return inner #4


@order_food #2 #5 -->inner function call
def throw_party(): #9
    print("throw party") #10
    

throw_party() #1   