def outer(ox):
    print("outer called..",ox)
    def inner(ix):
        print("innner called...",ix)
        return ix**2
    
    return inner

ans= outer(10)  
x = ans(100) #inner function call...
print(x)


#calulcate_bill(amount,isDis,pers)
#inner calulcat dis

#cal(10000,true,10)