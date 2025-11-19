#args...
#args is not keyword..
#tuple
def getUsers(*args):
    print(args)

getUsers()    
getUsers("ram","shyam","amit")


#def getEmployees(*emps,x):
def getEmployees(x,*emps): #second soln
    print(emps)  
    print(x)  

getEmployees("amit","sumit","shyam")    
#getEmployees("amit","sumit","shyam",x="ram")   #soln 