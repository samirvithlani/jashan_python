#write
#location file: present overri.... not present create write

#file == variable...
# file = open("demo.txt","a")
# file.write("hi this is using write() 2nd line")
# file.close()

# file = open("demo1.txt","a")
# file.writelines(["\nraj","\nparth","\njay"])
# file.close()

# file = open("demo2.txt","a")
# print("hi this is using print funciton()",file=file)
# file.close()

name = "ram"
age = 22

file = open("demo3.txt","a")
file.write(f"Name = {name}")
file.write(f"Age = {age}")
file.close()


#task:
# data = {"id":1,"name":"raj","age":23,"status":False}
# id = 1
# name = raj

score = [["virat",10,20,30],["rohit",23,44,56],["ms",90,78,34]]
# #virat score
# match 1 = 10
# match 2 = 30
