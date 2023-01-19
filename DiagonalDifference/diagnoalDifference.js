/*
Given a square matrix,
calculate the absolute difference between the sums of its diagonals.
*/

const diagonalDifference =()=>{
    let sumone = 0;
    let sumtwo = 0;

    arr.forEach((ele , ind, arr) => {
        sumone += ele[ind];
        sumtwo += ele[arr.length -1 -ind];
        console.log(sumone)
        console.log(sumtwo)
    })
    console.log(Math.abs(sumone - sumtwo));
}