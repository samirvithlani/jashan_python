def demo():
    print("demo called...")
    return 100


# x = demo() #calling
# print("x = ",x)

x = demo #it will call.. it will return an address to x
print("x = ",x)
#x == demo()
ans = x() #demo funciton call..
print("ans =",ans)