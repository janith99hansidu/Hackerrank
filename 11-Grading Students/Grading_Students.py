def gradingStudents(grades):
    # Write your code here
    output = []
    for grade in grades:
        if grade > 37:
            roudup_multiple = int(grade/5) +1
            if roudup_multiple*5 - grade < 3:
                result = int(roudup_multiple*5)
            else:
                result = grade
        else:
            result =grade
        output.append(result)
    return output
