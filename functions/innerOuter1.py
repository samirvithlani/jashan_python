# def outer(ox):
#     print("outer called..",ox)
#     def inner(ix):
#         print("innner called...",ix)
#         return ix**2
    
#     ans = inner(ox)
#     print(f"ans = {ans}")
#     return ans

# ans= outer(10)  
# print(f"ans = {ans}")


def outer(ox):
    print("outer called..",ox)
    def inner(ix):
        print("innner called...",ix)
        return ix**2
    
    return inner(ox)

ans= outer(10)  
print(f"ans = {ans}")
            