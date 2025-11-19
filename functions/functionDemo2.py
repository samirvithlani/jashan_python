def getUserData(name,email,age,salary):
    print(f"name  = {name}")
    print(f"email  = {email}")
    print(f"age  = {age}")
    print(f"salary  = {salary}")


#getUserData("amit","amit@gmail.com",23,45600)
#getUserData(23,"ram",34000,"ram@gmail.com") 
#named param
getUserData(age=23,name="ram",salary=34500,email="ram@gmail.com")
    