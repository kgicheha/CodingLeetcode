/*
Day 3: Intro to Conditional Statements

Given an integer, n, perform the following conditional actions:

    If n is odd, print Weird
    If  is even and in the inclusive range of 2 to 5, print Not Weird
    If  is even and in the inclusive range of 6 to 20 , print Weird
    If  is even and greater than 20 , print Not Weird

print 'Weird' if the number is weird, otherwise print 'Not Weird'

/*
Not Weird
    EVEN && n > 2 && n < 5
    EVEN n > 20
Weird
    ODD
    EVEN & n > 6 && n < 20
*/


const conditionalStatement = (n) => {
  if (n % 2 === 0) {
    if ((n > 2 && n < 5) || n > 20) {
      console.log("Not Weird");
    } else if (n > 6 && n < 20) {
      console.log("Weird");
    }
  } else {
    console.log("Weird");
  }
};

conditionalStatement(4);
conditionalStatement(14);
conditionalStatement(22);
