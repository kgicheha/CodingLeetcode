/*
Given five positive integers,
find the minimum and maximum values
that can be calculated by summing exactly four of the five integers.
Then print the respective minimum and maximum values as a single line
of two space-separated long integers.

EXAMPLE
arr =[1,3,5,7,9]
minimum sum = 1+3+5+7 = 16
maximum sum = 3+5+7+9 = 24
*/

/*
STEPS
    sort the values in the given array
    loop through array
        minSum = sum of all values, except the last value
        maxSum = sum of all values, except the first value
*/

const miniMaxSum =(arr)=>{
    let minSum = 0, maxSum = 0

    let sortedArr = arr.sort((a,b) => a-b)
    for(let i in sortedArr){
        if(i != sortedArr.length - 1) {
            minSum += sortedArr[i]
        }
        if(i != 0){
            maxSum +=sortedArr[i]
        }
    }
    console.log(minSum + " " + maxSum)
}

let arr = [1,3,5,9,7]
miniMaxSum(arr)
