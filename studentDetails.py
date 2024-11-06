student_marks ={}

def add_student(name, marks):
    student_marks[name]= marks

def calculate_average():
    if len(student_marks)==0:
       return 0
    total_mark = sum(student_marks.values())
    average_marks =total_mark/len(student_marks)
    return average_marks

num_of_students = int(input("Enter teh number of students:"))

for _ in range(num_of_students):
    name =input("Enter student name:")
    marks = int(input("Enter student marks:"))
    add_student(name,marks)

print("student marks :",student_marks)

average=calculate_average()
print("the average marks of students is",average)

