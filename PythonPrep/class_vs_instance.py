'''

Write a Person class with an instance variable, age ,
and a constructor that takes an integer, initialAge, as a parameter.
The constructor must assign initialAge to age
after confirming the argument initialAge passed as is not negative;
if a negative argument is passed as ,initialAge
    the constructor should set age to 0
    and print Age is not valid, setting age to 0..
 In addition, you must write the following instance methods:

    yearPasses() should increase the  instance variable by .
    amIOld() should perform the following conditional actions:
    If age < 13 , print You are young..
    If age>= 13 and  age < 18, print You are a teenager..
    Otherwise, print You are old..
'''


class Person:
    def __init__(self, initialAge):
        self.age = initialAge
        if initialAge < 0:
            self.age = 0
            print("Age is not valid, setting age to 0.")
        else:
            self.age = initialAge

    def amIOld(self):
        if self.age < 13:
            print("You are young.")
        elif self.age >=13 and self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self):
        self.age +=1


person1 = Person(-1)
person2 = Person(13)
person3 = Person(19)
person4 = Person(21)
person2.amIOld()
person3.amIOld()
person4.amIOld()