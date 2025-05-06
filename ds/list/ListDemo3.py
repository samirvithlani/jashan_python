data = [100,20,30,100,20,40,34,67]

x = data.count(100)
print("100 count is ",x)

ind = data.index(20)
print("20 index is ",ind)

data.sort(reverse=True)
print("sorted data is ",data)

lang = ["java","python","php",".net","c","c++"]
#lang.sort(key=len,)
lang.reverse()
print("sorted lang is ",lang)

