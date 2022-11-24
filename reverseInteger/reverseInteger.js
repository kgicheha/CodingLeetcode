const reverseInteger = (x)=> {
    // result = x.toString().split("").reverse().join("")

    let isNegative = false

    if(x < 0){
        isNegative = true
        x = -x
    }

    let reversedNum = 0

    while(x > 0){
        reversedNum *= 10
        let remainder = x % 10
        reversedNum += remainder
        x = Math.floor(x / 10)
    }

    if(reversedNum > Math.pow(2,31)-1 || reversedNum < Math.pow(-2,31))

    return isNegative ? -reversedNum : reversedNum
}

console.log(reverseInteger(123))
console.log(reverseInteger(0))
console.log(reverseInteger(-123))
console.log(reverseInteger(120))




//solution 1
    //1. if x is a negative, change it to a postive number
    //2. loop: while x is less than 0
        //3. create a variable to store the reversed number, which starts off as 0
        //4. multiply the reversed number by 10 through each iteration
            // this ensures that the digits in the reversed number variable are pushed to the left
        //5. get the remainder of x % 10 and store it to reversed number variable
        //6. change x to the result of x / 10.
            // round down the result using Math.floor
        //7. create an if statement that returns 0 if
            // the reversedNum is below or above the limit
        //8. return result
            // if x was a negative add a negative sign infront of the reversed number
            //else return the reversed Number


            //***EXAMPLE***
                // x = 123
                // let reverseNum = 0;

                //FIRST ITERATION
                // reverseNum = reverseNum * 10
                    //0
                // remainder = x % 10
                    // remainder = 123 % 10
                    // remainder =  3
                // reverseNum += remainder
                    // reverseNum = 0 + 3
                    // reverseNum = 3
                // x = Math.floor( x / 10)
                    //x = 12

                //SECOND ITERATION
                //reverseNum *= 10
                    //3 * 10
                    //30
                //remainder = x % 10
                    //remainder = 12 % 10
                    //remainder = 2
                //reverseNum += remainder
                    //30 = 30 + 2
                    //32
                //x = Math.floor(x / 10)
                    //x = 1

                //THIRD ITERATION
                //reverseNum *= 10
                    //32 = 32 * 10
                    //reverseNum = 320
                //remainder = x % 10
                    //remainder = 1 % 10
                    //remainder = 1
                //reverseNum += remainder
                    //reverseNum = 320 + 1
                    //reverseNum = 321
                //x= Math.floor(x / 10)
                    //x= 0

                //return reverseNum ? -reverseNum : reverseNum
                    //return 321
