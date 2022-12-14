/*
You are in charge of the cake for a child's birthday.
You have decided the cake will have one candle for each year of their total age.
They will only be able to blow out the tallest of the candles.
Count how many candles are tallest.

example
candles = [4,4,1,3]
max height is 4, so return 2 because thats how many times it appears
*/

/*
given: array of integers
edge cases: empty array --> return array

STEPS
    create variable that stores the max value
    create empty variable that keeps frequency count of the max value

    loop through given array
        if (a > b),
            a remains as max
            increase frequency count by 1
            move on to the next value in arry
        else if (b > a)
            set b as the new max value
            set the frequency count variable to equal 1

return: the frequency count of the biggest number
*/


const birthdayCakeCandles =(candles) =>{
    // Write your code here

    let maxValueFrequency = 0

    let maxValue = Math.max(...candles)

    for(let i in candles){
        if (candles[i] === maxValue){
            maxValueFrequency++
        }
    }
    console.log(maxValueFrequency)
}

let candles =[4,4,1,3]

birthdayCakeCandles(candles)