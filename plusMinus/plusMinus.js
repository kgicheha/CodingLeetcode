/*
Given an array of integers, calculate the ratios of its elements that are positive,
 negative, and zero. Print the decimal value of each fraction on a new line with
 places after the decimal.
 Example

 arr = [1,1,0,-1,-1]
 There are n =5 elements, two positive,
 two negative and one zero.
 Results are printed as:
result
0.400000
0.400000
0.200000

*/

const plusMinus = (arr) => {
    //BRUTE FORCE
//   let negativeVals = 0,
//     zeroVals = 0,
//     postiveVal = 0;

//   for (let i in arr) {
//     if (arr[i] < 0) {
//       negativeVals++;
//     } else if (arr[i] > 0) {
//       postiveVal++;
//     } else {
//       zeroVals++;
//     }
//   }
//   console.log((postiveVal/arr.length).toFixed(6))
//   console.log((negativeVals/arr.length).toFixed(6))
//   console.log((zeroVals/arr.length).toFixed(6))


  //OPTMIZED
const lengthOfPositiveVals = arr.filter((i) => i > 0).length
const lengthOfNegativeVals = arr.filter((i) => i < 0).length
const lengthOfZeroVals = arr.filter((i) => i===0).length

console.log((lengthOfPositiveVals/arr.length).toFixed(6))
console.log((lengthOfNegativeVals/arr.length).toFixed(6))
console.log((lengthOfZeroVals/arr.length).toFixed(6))
};

arr = [1, 1, 0, -1, -1];
plusMinus(arr);
