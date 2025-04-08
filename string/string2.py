data = "Hi lello"

#flag = data.startswith("A")
flag = data.startswith("A",1)
print("startsWith ",flag)
flag = data.endswith("it")
print("endsWith",flag)

print("isal",data.isalnum())
print(data.isalpha())
print(data.isdigit())
print(data.islower())
print(data.isupper())
print(data.isnumeric())
print(data.isspace())
print(data.isprintable()) #//false
print(data.istitle())


