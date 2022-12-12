/*
Calculate and print the sum of the elements in an array,
keeping in mind that some of those integers may be quite large.
*/

/*
STEPS:
    create a result variable and initialize it to 0
    traverse given array
        add each value to the initialValue
    return result variable
*/


const aVeryBigSum =(ar) => {
    // Write your code here

   //BRUCE FORCE
    // let result = 0
    // for(let i in ar){
    //     result += ar[i]
    // }

    //OPTOMIZED
    let initValue = 0
    const result = ar.reduce((accumulator, currVal)=> accumulator +currVal, initValue)

    return result

}

aVeryBigSum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005])
