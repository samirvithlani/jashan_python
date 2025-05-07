#list comprehension...
#creaate list using comprehension

data =[i for i in range(1,20)]
print(data)


users = ["ram","shyam","sam","suresh","ajay"]
#if else

filtList=[i for i in users if i[0] =="s"]

# for i in users:
#     if i[0] == "s":
#         filtList.append(i)

print(filtList) 

#if else
filtList2 = [i if i[0] =="s" else "" for i in users]       

print(filtList2)