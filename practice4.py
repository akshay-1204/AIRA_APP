"""Task Requirement: Student Grade Evaluation System using Nested if-elif
Build a Student Grade Evaluation System in Python using nested `if-elif-else statements.
Requirements
Create a program that accepts the following inputs:
Student name
Marks in 5 subjects
Mathematics
Science
English
Computer Science
Social Studies
Processing
Calculate:
Total marks
Percentage
Determine whether the student has passed or failed:
A student must score at least 35 marks in every subject to pass.
If the student passes, determine the grade using if-elif:
90–100 → Grade A+
80–89 → Grade A
70–79 → Grade B
60–69 → Grade C
50–59 → Grade D
35–49 → Grade E
If the student fails:
Identify the subjects in which the student scored below 35.
Display the result as Fail.
Additional Nested Condition
Use a nested if-elif-else to determine performance:
If percentage ≥ 90:
If percentage == 100 → "Outstanding"
Else → "Excellent"
Else if percentage ≥ 75:
"Very Good"
Else if percentage ≥ 60:
"Good"
Else:
"Needs Improvement"
Expected Output
Student Name: Rahul
Total Marks: 425 / 500
Percentage: 85.0%
Result: PASS
Grade: A
Performance: Very Good
"""
student_name = input("Enter your student name: ")

subject = {
    "maths": int(input("Enter your marks in maths: ")),
    "science": int(input("Enter your marks in science: ")),
    "english": int(input("Enter your marks in english: ")),
    "computer_science": int(input("Enter your marks in computer science: ")),
    "social_studies": int(input("Enter your marks in social studies: ")),
}

total_marks = (
    subject["maths"]
    + subject["science"]
    + subject["english"]
    + subject["computer_science"]
    + subject["social_studies"]
)
percentage = (total_marks / 500) * 100

if (subject["maths"] < 35 or
    subject["science"] < 35 or
    subject["english"] < 35 or
    subject["computer_science"] < 35 or
    subject["social_studies"] < 35):

    result = "FAIL"

else:
    result = "PASS"

if percentage >= 90:
    Grade = "A+"
elif percentage >= 80:
    Grade = "A"
elif percentage >= 70:
    Grade = "B"
elif percentage >= 60:
    Grade = "C"
elif percentage >= 50:
    Grade = "D"
elif percentage >= 35:
    Grade = "E"
elif percentage < 35:
    Grade = "Fail"

if percentage == 100:
    Performance = "Outstanding"
elif percentage >= 90 and percentage < 100:
    Performance = "Excellent"
elif percentage >= 75 and percentage < 90:
    Performance = "Very Good"
elif percentage >= 60 and percentage < 75:
    Performance = "Good"
elif percentage < 60:
    Performance = "Needs Improvement"
else:
    Performance = "Fail"

if result == "PASS":

    report = f"""
========================================
        STUDENT GRADE REPORT
========================================

Student Name : {student_name}

Mathematics      : {subject["maths"]}
Science          : {subject["science"]}
English          : {subject["english"]}
Computer Science : {subject["computer_science"]}
Social Studies   : {subject["social_studies"]}

----------------------------------------
Total Marks : {total_marks} / 500
Percentage  : {percentage}%

Result      : {result}
Grade       : {Grade}
Performance : {Performance}

========================================
"""

else:

    report = f"""
========================================
        STUDENT GRADE REPORT
========================================

Student Name : {student_name}

Mathematics      : {subject["maths"]}
Science          : {subject["science"]}
English          : {subject["english"]}
Computer Science : {subject["computer_science"]}
Social Studies   : {subject["social_studies"]}

----------------------------------------
Total Marks : {total_marks} / 500
Percentage  : {percentage}%

Result      : {result}

NEED A PARENT MEETING

========================================
"""

print(report)