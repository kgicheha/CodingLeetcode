/*
Reverse an array of integers.
*/


/*
given: [1,2,3]
STEPS
    create empty array
    loop given array
        pop the last integer and store it to the array
    return the new array


return [3,2,1]
*/
const reverseArray =(a)=>{
let revArray = []

for(let i = a.length-1; i >= 0 ; i--){
    revArray.push(a[i])
}

console.log(revArray)
}


reverseArray([1,2,3])

