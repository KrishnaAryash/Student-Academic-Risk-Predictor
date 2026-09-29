from student import addastudent
from student import showstudents
from student import searchstudent
from student import deleteastudent
from student import students
from attendance import attendance_status
from marks import marks_status
from analysis import calculate_score
from risk import find_risk
from recommendation import give_recommendation
def analyze_onestudent():
    if len(students) == 0:
        print("No students available.")
        return

    reg_no = input("Enter the registration number: ")
    found = False
    for student in students:
        if student["reg_no"] == reg_no:
            found = True
            att_result = attendance_status(student["attendance"])
            marks_result = marks_status(student["marks"])
            score = calculate_score(student["attendance"],student["marks"],student["quiz"],
                                    student["assignment"],student["previous_result"],)

            risk = find_risk(score)
            recommendation = give_recommendation(risk)
            print("\n-- Student Analysis --")
            print("Student Name:", student["name"])
            print("Attendance:", att_result)
            print("Marks:", marks_result)
            print("Performance Score:", round(score, 2))
            print("Risk Level:", risk)
            print("Recommendation:", recommendation)
            break
    if not found:
        print("STUDENT NOT FOUND.")
def class_summary():
    if len(students) == 0:
        print("No students available.")
        return

    print("\n-- Class Summary --")
    total = 0
    for student in students:
        score = calculate_score(
            student["attendance"],
            student["marks"],
            student["quiz"],
            student["assignment"],
            student["previous_result"],
        )
        
        total += score
        print(student["name"], ":", round(score, 2))

    avg = total / len(students)
    print("Class Average:", round(avg, 2))
def main():
    while  True:
        print("\n_________________________________")
        print("  STUDENT ACADEMIC RISK PREDICTOR    ")
        print("_________________________________")
        print("1. Add a Student")
        print("2. Show Students")
        print("3. Search for a Student")
        print("4. Analyze  a Student")
        print("5. Get Class Summary")
        print("6. Delete a Student")
        print("7. Exit")
        choice = input("Enter your choice: ") # Choice of the user is entered
        if choice =="1":
            addastudent()
        elif choice ==  "2":
            showstudents()
        elif choice == "3":
            searchstudent()
        elif choice == "4":
            analyze_onestudent()
        elif choice =="5":
            class_summary()
        elif choice == "6":
            deleteastudent()
        elif choice == "7" :
            print("PROGRAM ENDED.")
            break
        else:
            print("CHOICE IS INVALID.")   # PRINTED IF USER ENTERS INVALID CHOICE
main()
