def validate_grade(student):
    if type(student[1]) != int:
        print("Skipped student: grade must be an int")
        return False

    if student[1] < 0 or student[1] > 100:
        print("Skipped student: grade must be between 0-100")
        return False

    return True