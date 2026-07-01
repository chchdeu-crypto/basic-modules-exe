from data_list import students
from student_validation import validate_student
from grade_validation import validate_grade
from grade_logic import print_grade_status
from average_calculation import average_calculation
def main():
    grade_total=[]
    for student in students:
        if validate_student(student):
            if validate_grade(student):
                grade_list=print_grade_status(student)
                grade_total.append(grade_list)
    average_calculation(grade_total)



main()