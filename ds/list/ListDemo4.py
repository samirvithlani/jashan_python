#players = [["virat",82],["sachin",100],["dhoni",30]]

players =[]
for i in range(3):
    name = input("Enter player name: ")
    score = int(input("Enter player score: "))
    players.append([name,score])

for i in players:
    for j in i:
        print(j,end=" ")
    print()


name = input("enter player name to search: ")
found = False
for  i in players:
    if i[0]==name:
        print("player found")
        print(i)
        found = True
        break

if not found:
    print("player not found")     
    
#sort 2d list..
       