# list of three students named Jon, Kim and Lee
students = ["Jon", "Kim", "Lee"]
students.append("Sara")
students.append("Miko")
 #change Jon to John
students[0] = 'John'
# greet each student and print the total number of students
def greet_students(students):
    for student in students:
        print(f"Hi {student}")
    print(f"Total students: {len(students)}")

# call the function
greet_students(students)




# Task A complete
# Task C complete

# Task D complete
