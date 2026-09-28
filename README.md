## Student Academic Risk System

## 1. Project Overview:
The Student Academic Risk System is a Python-based project designed to analyze the academic performance of students using basic programming and rule-based decision-making.The system stores student academic information such as attendance, marks, quiz performance, assignment performance, and previous results. It calculates an overall performance score and uses predefined rules to identify the student's academic risk level.
The project is developed using basic Python concepts such as functions, lists, dictionaries, loops, conditional statements, modules, and arithmetic calculations.
---

## 2. Features
The project provides the following features:
- Add a new student
- Display all student records
- Search for a student using registration number
- Analyze an individual student's performance
- Calculate an overall performance score
- Check attendance status
- Check marks status
- Identify academic risk level
- Provide recommendations based on risk level
- Display class performance summary
- Delete a student record
---

## 3. Technologies / Tools Used
- Programming Language: Python
- Code Editor: Visual Studio Code
- Version Control: Git / GitHub
- Data Structure: Python List and Dictionary
- Data Storage: In-memory storage using Python lists
No machine learning model or external AI library is used in this project. The risk analysis is based on predefined rules.

## 4. Project Structure
```text
Student_Academic_Risk_System/
│
├── main.py
├── student.py
├── attendance.py
├── marks.py
├── analysis.py
├── risk.py
├── recommendation.py
├── README.md
├── statement.md
└── .gitignore
```
## File Description
- "main.py" - Contains the main menu and controls the overall program.
- "student.py" - Handles adding, displaying, searching, and deleting student records.
- "attendance.py" - Checks the attendance status of a student.
- "marks.py" - Checks the marks status of a student.
- "analysis.py" - Calculates the student's overall performance score.
- "risk.py" - Determines the student's academic risk level.
- "recommendation.py" - Provides recommendations based on the risk level.
- "README.md" - Contains project information and instructions.
- "statement.md" - Contains the project problem statement and scope.
- ".gitignore" - Contains files and folders that should not be uploaded to GitHub.
---

## 5. Performance Score Calculation
The system calculates the performance score using the following weightages:
Academic Factor| Weightage
Attendance     | 25%
Marks          | 30%
Quiz           | 15%
Assignment     | 15%
Previous Result| 15%

The total weight is 100%.
The formula used is:
Performance Score =
(Attendance × 0.25) +(Marks × 0.30) +(Quiz × 0.15) +(Assignment × 0.15) +(Previous Result × 0.15)
---
## 6. Risk Classification
The calculated performance score is classified into three risk levels:

Score         | Risk Level
75 or above   | Low Risk
50 to below 75| Medium Risk
Below 50      | High Risk
The system then provides a recommendation according to the identified risk level.
---
## 7. Installation and Running
   1. Install Python on your computer.
   2. Open the project folder in Visual Studio Code.
   3. Open the terminal in VS Code.
   4. Run the following command:  python main.py
---
## 8. How to Use the Program
After running the program, a menu will be displayed:
   1. Add Student
   2. Show Students
   3. Search Student
   4. Analyze Student
   5. Class Summary
   6. Delete Student
   7. Exit
Enter the corresponding number to select an operation.
#Example
To analyze a student:
   1. Select option "4".
   2. Enter the student's registration number.
   3. The system displays:
      - Student name
      - Attendance status
      - Marks status
      - Performance score
      - Risk level
      - Recommendation
      ---

## 9. Testing Instructions
The following operations can be tested:
   - Add one or more students.
   - Use Show Students to check the stored records.
   - Search for an existing registration number.
   - Search for a registration number that does not exist.
   - Analyze an existing student.
   - Check whether the performance score and risk level are displayed.
   - View the class summary.
   - Delete an existing student.
   - Try an invalid menu option.
   - Exit the program.
Expected Result-
The program should correctly perform the selected operation and display an appropriate message or result.

