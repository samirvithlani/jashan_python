data = {"Guj":"Gandhinagar","Mah":"Mumbai","UP":"lucknow","Guj":"Ahmedabad"}
print(data)
#update
data["Guj"]="Surat"
print(data)
#add
data["Punjab"]= "chandigadh"
print(data)
#
data.update({"Guj":"Ahm","Raj":"Jaipur"})
print(data)


removedValue = data.pop("Raj")
print("removing ...",removedValue)
print(data)

removedData = data.popitem()
print("removing...",removedData)
print(data)

