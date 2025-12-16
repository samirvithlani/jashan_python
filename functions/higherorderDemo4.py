def science(name):
    print(f"{name} admission in science confirmed")
    return f"{name} welcome to science"
    
def comm(name):
    print(f" {name} admission in comm confirmed")    
    return f"{name} welcome to comm"

def arts(name):
    print(f" {name} admission in arts confirmed")    
    return f"{name} welcome to arts"
    

def admission(cb,name):
    print("admission function called...")
    #cb("amit")
    message = cb(name)
    print("message ",message)

pers = int(input("enter pers :"))    
name = input("enter Name :")
if pers>=80:
    admission(science,name)
elif pers>=70:
    admission(comm,name)    
elif pers>=60:
    admission(arts,name)    
        