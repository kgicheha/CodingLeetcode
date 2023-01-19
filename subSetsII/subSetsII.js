
/*
    DEPTH FIRST SEARCH RECURSIVE ALGORITHM
    create empty array to store the results


    depth first search recursive algo
    trverse list

    return an array of all the UNIQUE subsets

    TIME COMPLEXITY: O(2 )
*/

const subsets = (nums, depth = 0, subset =[], results = []) =>{

    //if you reach the last number in the given array,
        //push your subsets to the results array
    //else
   if(depth === nums.length) {
    results.push(subset)
   } else {
    subsets(nums, depth + 1, subset, results)
    subsets(nums, depth + 1, [...subset, nums[depth]], results)
   }
   console.log(results)
   return results

}

subsets([1,2,3])
// subsets([0])