#sum
nums = [1,2,3]
print(sum(nums))
print(min(nums))
print(max(nums))

students = [{"name":"raj","marks":80},{"name":"neha","marks":86}]

topper = max(students,key= lambda x:x["marks"])
print(topper)

#reversed
print(list(reversed(nums)))


#all
marks = [89,90,70]
print(all(m>=60 for m in marks))
print(any(m>=91 for m in marks))

#zip
names = ["jasan","raj","parth"]
score = [90,78,87]

for x,y in zip(names,score):
    print(x,y)


#enumerate
names = ["jasan","raj","parth"]

for index,value in enumerate(names):
    print(index,value)

#sorted..
students = [("Ram", 80), ("Shyam", 95), ("Amit", 70)]
ans = sorted(students,key= lambda x:x[1],reverse=True)
print(ans)
