
def print_grade_status(student):
    grade = student[1]
    

    if grade >= 90:
        print(student[0],student[1] ,"- Excellent")
        
        
    elif grade >= 60:
        print(student[0],student[1], "- Pass")
        
        
    else:
        print(student[0], student[1], "- Fail")
    return grade   
       
