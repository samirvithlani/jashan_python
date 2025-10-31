list = [[1,2],[3,4],[5,6]]

# for i in list:
#     for j in i:
#         print(j)

for i,j in list:
    print(i,j)
    


a = [11,22,33]    
b = [44,55,66]

for i,j in zip(a,b):
    print(i+j)