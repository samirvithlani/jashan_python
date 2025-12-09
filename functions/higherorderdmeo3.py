def science(name):
    
    print(f"{name} admission in science confirmed")
    
def comm(name):
    print(f" {name} admission in comm confirmed")    

def arts(name):
    print(f" {name} admission in arts confirmed")    
    

def admission(cb,name):
    print("admission function called...")
    #cb("amit")
    cb(name)

pers = int(input("enter pers :"))    
name = input("enter Name :")
if pers>=80:
    admission(science,name)
elif pers>=70:
    admission(comm,name)    
elif pers>=60:
    admission(arts,name)    
        