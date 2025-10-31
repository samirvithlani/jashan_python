# data = {}
# print(data)
# print(type(data))

data = {"Guj":"Gandhinagar","Mah":"Mumbai","UP":"lucknow","Guj":"Ahmedabad"}
print(data)

k = data.keys()
print(list(k))
v = data.values()
print(v)
kv = data.items()
print(kv)

#access
#print(data["Guj"]) #if key is not present ex..
print(data.get("Guj1")) #None

for i,j in data.items():
    print(i," ",j)