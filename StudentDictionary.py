#Create a dictionary to store the name, roll_no, and total_mark of N students.Now print the details of the student with the highest total_mark.

def get_student_data():
    name = input("Enter the student's name: ")
    roll_no = input("Enter the student's roll number: ")
    total_marks = float(input("Enter the student's total marks: "))
    return {"name": name, "roll_no": roll_no, "total_marks": total_marks}

def main():
    students = []
    
    N = int(input("Enter the number of students: "))
    
    for _ in range(N):
        student_data = get_student_data()
        students.append(student_data)
    
    if students:
        highest_marks_student = max(students, key=lambda x: x['total_marks'])
        print("\nStudent with the highest total marks:")
        print(f"Name: {highest_marks_student['name']}")
        print(f"Roll No: {highest_marks_student['roll_no']}")
        print(f"Total Marks: {highest_marks_student['total_marks']}")

if __name__ == "__main__":
    main()
