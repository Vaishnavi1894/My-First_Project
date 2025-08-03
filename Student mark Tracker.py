students = {}

num_students = int(input("Enter the number of students:"))

for i in range(num_students):
    name = input(f"Enter the name of the student{i+1}:")
    marks = []
    subjects = int(input("Enter the total number of subjects: "))

    for j in range(subjects):
        mark = int(input(f"Enter mark{j+1}: "))
        marks.append(mark)
    students[name] = marks

def get_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"


for name,marks in students.items():
    total = sum(marks)
    average = total/len(marks)
    grade = get_grade(average)

    print(f"Name : {name}")
    print(f"Marks : {marks}")
    print(f"Total : {total}")
    print(f"Average : {average}")
    print(f"Grade : {grade}")


