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



def gradingStudents(grades):
    for i in range(0, len(grades)):
        print(grades[i])


grades = [73, 67, 38, 33]
gradingStudents(grades)