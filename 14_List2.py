marks = []
for i in range (0,6) :
    stu = int(input("Enter Marks of Student\n"))
    marks.append(stu)
print("unsorted marks = ",marks)
marks.sort()
print(marks)