student={}

def calculateAverage(Mark):
    return sum(Mark)/len(Mark)

n=int(input("Enter the number of students"))

for i in range(n):
    name=input(f"enter teh name of student {i+1}:")

    mark1=int(input("enter mark 1:"))
    mark2=int(input("enter the mark2:"))
    mark3=int(input("enter the mark3:"))
    student[name]=[mark1,mark2,mark3]

for name,mark in student.items():
    avg_marks=calculateAverage(mark)
    print(f"\n{name}s' mark:{mark}")
    print(f"the average marks of {name} is {avg_marks}")