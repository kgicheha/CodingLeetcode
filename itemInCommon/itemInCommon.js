/*
Return true or false if two arrays have any items in common
*/

/*
USING HASH TABLE
STEPS:
1. create empty hash table
2. loop though 1st array and store the items inside of the hash table
3. loop though 2nd array
    search to see if any item is in the hash table
    if it is, return true
4. return false

TIME COMPLEXITY: O(2N) -> 0(N) because you only have to loop through each array once
SPACE COMPLEXITY: O(N)
*/

const itemInCommon = (arr1, arr2) => {
  const itemsHashTable = {};
  for (let i = 0; i < arr1.length; i++) {
    itemsHashTable[arr1[i]] = true;
  }
  for (let j = 0; j < arr2.length; j++) {
    if (itemsHashTable[arr2[j]]) {
      return true;
    }
  }
  return false
};
let array1 = [1, 3, 5];
let array2 = [2, 4, 4];
itemInCommon(array1, array2);
