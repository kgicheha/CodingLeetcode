// merge Helper Function
// puts the array back together
function merge(arr1, arr2) {
  let combined = [];
  let i = 0;
  let j = 0;

  while (i < arr1.length && j < arr2.length) {
    if (arr1[i] < arr2[j]) {
      combined.push(arr1[i]);
      i++;
    } else {
      combined.push(arr2[j]);
      j++;
    }
  }

  while (i < arr1.length) {
    combined.push(arr1[i]);
    i++;
  }
  while (j < arr2.length) {
    combined.push(arr2[j]);
    j++;
  }

  return combined;
}

function mergeSort(arr) {
  if (arr.length === 1) return arr;

  let mid = Math.floor(arr.length / 2);
  let left = arr.slice(0, mid);
  let right = arr.slice(mid);

  return merge(mergeSort(left), mergeSort(right));
}

console.log(mergeSort([1, 3, 7, 8, 2, 4, 5, 6]));


/*
uses recursion
    1. breaks arrays in half
    2. has base case: when array.length is 1
        once it gets to the base case, thats when we use the merge function to put the array together


Based on Divide and Conquer
The given array is recursively divided into halves until it cannot be further divided. Then combined in a sorted manner
Time Complexity: O(n log n) → takes log n to break the elements into individual arrays. It takes n to put them back together.
Space Complexity: O(n) → creating new arrays
Process:
	Will create two functions: one that divides the arrays into halves, another that puts it back together
	Function 1: dividing into halves
		Base case: if the length of the array is equal to 1, return the array
		Create three variables
			Variable 1: midpoint of the array
			Variable 2: left side of the array
			Variable 3: right side of the array
		Pass the left and the right array recursively to the function 2 which will merge the two array

	Function 2: merge
		Create an empty array that will store the result

		Compare the two arrays,
			If the value on the 1st array is less than the value on the 2nd array
				Push the value on the 1st array to the result array
				Increment the pointer on the 1st array by 1
			Else:
				Push the value of the right array to the result array
				Increment the pointer on the 2nd array by 1
		If there are still values left on either array
			Push those value to the result array

		Return combined array

*/
