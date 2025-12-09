def science():
    print(f"admission in science confirmed")
    
def comm():
    print(f"admission in comm confirmed")    

def arts():
    print(f"admission in arts confirmed")    
    

def admission(cb):
    print("admission function called...")
    cb()

pers = int(input("enter pers :"))    
if pers>=80:
    admission(science)
elif pers>=70:
    admission(comm)    
elif pers>=60:
    admission(arts)    
        