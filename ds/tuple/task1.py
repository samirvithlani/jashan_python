records = [("Alice", "Math", 80), ("Alice", "Science", 90),
           ("Bob", "Math", 70), ("Bob", "Science", 60)]


data = []
names = []  
for name, subject, marks in records:
    if name not in names:
        data.append((name, marks))
        names.append(name)

    

# Step 2: Calculate averages
output = []
for item in data:
    name = item[0]
    total = 0
    count = 0
    for rec in records:
        if rec[0] == name:
            total += rec[2]
            count += 1
    avg = total / count
    output.append((name, avg))

print(output)
