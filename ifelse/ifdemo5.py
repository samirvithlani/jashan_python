#true false--->

age = int(input("enter age"))

if age>=18:
    print("you are allowed to enter in restaurant..")
    if age>=21:
        print("you are allowed in bar")
        if age>=25:
            print("you can play casino games...")
        else:
            print("you can not play games..")    
    else:
        print("you are not allowd in bar")    
    
else:
    print("you are allowed to enter in even restaurant.. stay in childern area")
    if age<=5:
        print("you can have ipads")
    else:
        print("you have to watch tv")    