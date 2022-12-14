/*

Write a program that prints a staircase of size n.


EXAMPLE
This is a staircase of size n = 4
   #
  ##
 ###
####
Its base and height are both equal to n . It is drawn using # symbols and spaces.
*/

/*

1
11
111
1111


STEPS
create empty string variable
while i < n:
    add '#' to string variable
    print the string variable
        https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/padStart
        use padstart to print the '#' at the end
            works similar to padding in css
            takes two arguments(length of pad, what to print)
        padstart


RESULT: print a staircase of n steps
*/

const staircase = (n) => {
  // Write your code here
  let stairs = "";
  let i = 0;
  while (i < n) {
    stairs += "#";
    console.log(stairs.padStart(n, ' '));
    i++;
  }
};

staircase(4)