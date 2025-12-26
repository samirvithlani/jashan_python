#read data from file
#file ust present at that path...

# file = open("demo1.txt","r")
# #x = file.read(1)
# x = file.read()
# print(x)
# file.close()

with open("demo1.txt","r") as file:
    # x =file.readline()
    # print(x)
    
    while True:
        x = file.readline()
        print(x,end="")
        if not x:
            break
    #file auto close..


with open("th.txt","r") as f:
    # x = f.readlines()
    # print(x)    
    for i in f.readlines():
        print(i,end="")
