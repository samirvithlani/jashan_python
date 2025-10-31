#dict
#{1:1,2:2,3:3,4:4,5:5}

data = {i:i  for i in range(1,6)}

# for i in range(1,6):
#     data[i]=i

data = {i:i**2 for i in range(1,6)}

print(data)    


#list
users = ["ram","shyam","amit","sumit","gita"]
#{"ram":3}

userwithlen = {i: len(i) for i in users}
print(userwithlen)

userwithlable = {i[0]:i for i in users}
print(userwithlable)

#if
userwithlen2 = {i:len(i) for i in users if len(i)>3}
print(userwithlen2)

#if("" else "")

#banana
#{b:1,a:3,b:2}
text= "banana"

x = {i:text.count(i) for i in text }
print(x)

#keys = ["name","age","city"]
#values =["samir",23,"ahm"]
#output {"name":"samir",.....}

#data = {a:1,b:2,c:3}
#data= {1:a,2,b,3:c}


sent = "hello world from python"
vovels = "aeiou"

#{"hello":2,"world":1}

vovel_count = {word:sum(1 for c in word if c in vovels)for word in sent.split(" ")}
print(vovel_count)