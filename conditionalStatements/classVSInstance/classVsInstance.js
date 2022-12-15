/*
Write a Person class with an instance variable, age,
and a constructor that takes an integer, initialAge, as a parameter.
The constructor must assign initialAge to age after confirming
the argument passed as initialAge is not negative;
if a negative argument is passed as initialAge ,
the constructor should set age to 0 and
print Age is not valid, setting age to 0..


In addition, you must write the following instance methods:

    1. yearPasses() should increase the age instance variable by 1.
    2. amIOld() should perform the following conditional actions:
        If age < 13, print You are young..
        If age >= 13 and age <= 18, print You are a teenager..
        Otherwise, print You are old..
*/

class Person {
  constructor(initialAge) {
    if (initialAge >= 0) {
      this.age = initialAge;
    } else {
      this.age = 0;
      console.log("Age is not valid, setting age to 0..");
    }
  }
  yearPasses() {
    this.age++;
  }
  amIOld(){
    if(this.age < 13){
        console.log('You are young.')
    } else if((this.age >= 13) && (this.age < 18)){
        console.log('You are a teenager.')
    }else {
         console.log('You are old.')
    }
  }
}

let person1 = new Person(4)
let person2 = new Person(-1)
let person3 = new Person(10)
let person4 = new Person(16)
let person5 = new Person(18)
console.log(person5.amIOld())
