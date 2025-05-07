data = ("ram","shyam", "sita", "gita")
dataList = list(data)
dataList[0] = "ravi"
data = tuple(dataList)
print(data)  # ('ravi', 'shyam', 'sita', 'gita')