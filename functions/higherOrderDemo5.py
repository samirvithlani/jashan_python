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
    # message = cb(name)
    # #print("message ",message)
    # return message
    return cb(name)

pers = int(input("enter pers :"))    
name = input("enter Name :")
confimMessage = None
if pers>=80:
    confimMessage = admission(science,name)
elif pers>=70:
    confimMessage = admission(comm,name)    
elif pers>=60:
    confimMessage = admission(arts,name)    

print(confimMessage)    
        