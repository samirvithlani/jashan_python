choice = int(input("press 1 for add \n press 2 for sub \n press 3 for mul \n press 4 for div"))

match choice:
    case 1:
        ans = 10 +20
        print("ans = ",ans)
    case 2:
        ans = 10 -20
        print("ans = ",ans)
    case _:
        print("invalid choice")
        
        
            

