'''
HackerLand University has the following grading policy:

    Every student receives a grade in the inclusive range from 0 to 100.
    Any  less than  is a failing grade.

Sam is a professor at the university and likes to round each student's grade according to these rules:

    If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5 .
    If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.


Given the initial value of  for each of Sam's  students,
write code to automate the rounding process.
'''

'''
EXAMPLES

grade = 84 round to 85 (85 - 84 is less than 3)
grade = 29 do not round (result is less than 40)
grade = 57 do not round (60 - 57 is 3 or higher)
'''

'''
GIVEN: an array of grades
STEPS:
    if grade is more than or equal to 38:
        if the remainder of the grade when divided by 5 is equal to either 3 or 4:
            round up the number
RESULT:
    return the grades after rounding as appropriate

'''


def gradingStudents(grades):
    for i in range(len(grades)):

        if grades[i] >= 38:
            if grades[i] % 5 == 3 or grades[i] % 5 == 4:
                grades[i] = grades[i] + (5 - grades[i] % 5)

    return grades



grades = [73, 67, 38, 33]
print(gradingStudents(grades))