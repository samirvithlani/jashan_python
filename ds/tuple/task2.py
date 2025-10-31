students = [(101, "Alice"), (102, "Bob"), (101, "Alice Duplicate"),(103, "Alice Duplicate"),(103, "Alice Duplicate")]

ids = []
duplicates = []

for student in students:
    student_id = student[0] #101,102,101,103,103
    if student_id in ids: #101,102,101,
        if student_id not in duplicates: #101,102
            duplicates.append(student_id) #101,102
    else:
        ids.append(student_id)#103,101 

print(duplicates)
