set1 = {"ram","seeta","lakshamn","hanuman","shankar"}
set2 = {"krishna","arjun","draupadi","hanuman","shankar"}

x = set1.union(set2)
x  =  set2 |set1
print(x)

x = set1.intersection(set2)
x = set1 & set2
print(x)

x = set2.difference(set1)
x = set1 - set2
print(x)

x = set1.symmetric_difference(set2)
print(x)

# set1.difference_update(set2)
# print(set1)

goa={"amit","sumit","ram","priya","krish"}
mumbai = {"ajay","jay","vijay","amit","priya"}
pune  = {"ajay","neha","amit","sukanya","nidhi","jay"}

#who have attended all eents
#who have attened goa mumbai but not pune
#who have attended goa and mumbai both
#who have attended mumbai and pune both but not goa
# who havee attended only pune