# data = set({})
# print(data)

data = {100,20,89,34,56,78,90,10,100,34}
print(data)
#print(type(data))

data.add(77)
print(data)

removedElm = data.pop()
print("removing...",removedElm)
print(data)
if 566 in data:
    data.remove(566) #key error
else:
    print("566 is not found")    
print(data)

data.discard(20)
print(data)

for i in data:
    print(i)





#pop ->    