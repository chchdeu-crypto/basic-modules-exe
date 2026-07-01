stundents=[
         ("Dana", 82),
    ("Tom", 55),
    ("Maya", 91),
    ("Ron", 60),
    ("Noa", "88"),
    ("Ben", 120),
    ("Lior", -5),
    (55, 70),
    ["bob",5] 
]
#check if grade is a number and between 0-100
def check_list_if_num_and_bet_0_100():
     for student in stundents:
          if type.student[1]==int:
               if 0<student[1]>100:
                    return student
               else:
                    return "skipped student: grade must be between 0-100"
passed_students=0
averge=0
grade_fo_average=0
for student in students:
        if type(student)==tuple:
            if type(student[0])!=str:
                print("skipped student: name must be string")
            elif type(student[1])==int:
                if  0<student[1]<100:
                    if student[1]>90:
                        print(student[0],student[1],"exelent")
                        passed_students+=1
                        averge+=student[1]
                        grade_fo_average+=1
                    elif  60<=student[1]<90:
                        print(student[0],student[1],"pass")
                        passed_students+=1
                        averge+=student[1]
                        grade_fo_average+=1
                    elif student[1]<60:
                        print(student[0],student[1],"failed")
                        averge+=student[1] 
                        grade_fo_average+=1
                        
                        
                else:
                        print("skipped student: grade must be between 0-100")
            elif type(student[1])!=int:
                print("skipped student: grade must be an int")
        else:
             print("skipped student: data must be a tuple")
print(f"passed students: {passed_students}")
print("averge:", averge/grade_fo_average)