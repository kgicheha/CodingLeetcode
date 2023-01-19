/*
Given a string, S , of length N that is indexed from 0 to N-1 ,
print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).

Note: 0 is considered to be an even index.


S= adbecf

Print abc def
*/

/*
GIVEN: string
STEPS:



RETURN: 2 strings
        string1= even numbered characters
        string2= odd numbered characters

*/

const processData = (input) => {
  let evenNumString = "",
    oddNumString = "";

  let inputCopy = input.split("\n").slice(1);

  for (let i in inputCopy) {
    i % 2 === 0 ? (evenNumString += inputCopy[i]) : (oddNumString += inputCopy[i]);
  }

  console.log(`${evenNumString}\n ${oddNumString}`);
};
processData("adbecf");
