users = ["amit","ajay","kunal","shyam","raj"]
print(users)

#add
users.append("ravi")
print(users)
users.extend(["rajkumar","suresh"])
#users.extend("GOA")
print(users)
users.insert(1,"parth")
print(users)



#remove...
#removedElm = users.pop() #remove last element,,,
removedElm = users.pop(2) #remove last element,,,
print("removing....",removedElm)
print(users)
if "raja" in users:
    users.remove("raja")
else:
    print("raja not found")
print(users)

