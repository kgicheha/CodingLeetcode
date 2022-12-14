/*
Given the meal price (base cost of a meal),
tip percent (the percentage of the meal price being added as tip),
 and tax percent (the percentage of the meal price being added as tax) for a meal,
find and print the meal's total cost. Round the result to the nearest integer.
*/

/*
Given:
1) base meal price,
2) tip percentage
3) tax percent

edge cases:
STEPS

create a class that
    takes in the given items,
    convert percentages into decimals
        let tip = (meal_cost / 100) * 20
        let tax = (tax_percent / 100) * meal_cost

    calculates the total price
        total = baseMealPrice + tip + tax


RETURN: total cost of meal in whole number
*/

const solve = (meal_cost, tip_percent, tax_percent)=> {
    // Write your code here
   let tip = (tip_percent / 100) * meal_cost
    let tax = (tax_percent / 100) * meal_cost

    let total = Math.floor(meal_cost + tip + tax)
    console.log("Your total is " + total)

}

solve(12, 20, 8)