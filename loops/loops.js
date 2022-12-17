/*
Given an integer, n , print its first 10 multiples.
Each multiple n*1 (where 1 <= i <= 10 )
should be printed on a new line in the form: n x i = result.
*/

const loopEquation = (n) => {
  let i = 1;
  while (i <= 10) {
    let result = n * i
    console.log(n + " x  " + i + " = " + result )
    i++
  }
};

loopEquation(3)
