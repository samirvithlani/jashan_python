city = "ahmedabad"

print(city[::-1])
print(city[::-2])
print(city[::1])
print(city[::2])
x = city[::-1]
print(x)

print(city[1::1])
print(city[1::2])

a  = "naman"

if a == a[::-1]:
    print("palindrome")